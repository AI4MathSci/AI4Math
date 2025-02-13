# This code accepts a model name, such as "gpt-4", model="gpt-4o-mini", etc., a math problem and a parameter max_retreies. 
# It calls an the LLM API with the model name to request it to generate solution steps, and generate the corresponding 
# Python code for the solution. It then calls the corresponding Python functions to solve the problem. 
# If there is error in executing the Python code, it will re-prompt the LLM to re-generate the code with a 
# fix to the error until a successful execution of the code or max retires has been exhausted

from openai import OpenAI
import subprocess
import argparse


#Note: the env var "OPENAI_API_KEY" must have been set before calling OpenAI()
client = OpenAI()

# model could be "gpt-4", model="gpt-4o-mini", etc.
def call_openai_api(model, prompt):
    response = client.chat.completions.create(
        #model="gpt-4",
        #model="gpt-4o-mini",
        model = model,
        messages=[
            {"role": "user", "content": f"You are an AI assistant that generates Python code using SciPy, NumPy, or SymPy to solve mathematical problems, if you put in any lne that is not code, start it with a # so it becomes a comment line, also do not add lines such as ```python and ```, make sure to include code to print the result: {prompt}"}
        ]
    )

    return response.choices[0].message.content

def execute_python_code(code):
    try:
        result = subprocess.run(["python3", "-c", code], text=True, capture_output=True)

        if result.returncode == 0:
            print("Execution Output:\n", result.stdout)
            return True, result.stdout
        else:
            print("Execution Error:\n", result.stderr)
            return False, result.stderr
    except Exception as e:
        return False, str(e)

def print_generated_code(code):
    print("Generated Code:")
    print("=" * 40)
    print(code)
    print("=" * 40)

def main():
    parser = argparse.ArgumentParser(description="Solving math problems")
    parser.add_argument("--model", required=True)
    parser.add_argument("--problem", required=True)
    parser.add_argument("--max_retries", type=int, required=True)

    args = parser.parse_args()
    model =args.model 
    prompt = args.problem
    max_retries = args.max_retries

    for attempt in range(max_retries):
        generated_code = call_openai_api(model, prompt)
        print_generated_code(generated_code)

        success, output = execute_python_code(generated_code)

        if success:
            print("Successfully executed the code.")
            break
        else:
            print(f"Attempt {attempt + 1} failed. Regenerating code...")
            prompt = f"The following code failed with an error:\n{generated_code}\nError message:\n{output}\nPlease correct it and regenerate the Python code to solve: {math_problem}"
    else:
        print("Max retries reached. Unable to generate working code.")

if __name__ == "__main__":
    main()
