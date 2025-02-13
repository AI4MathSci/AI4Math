# Try it out
slover.py accepts the following args:
- model name, such as "gpt-4", model="gpt-4o-mini", etc.,
- A math problem
- A parameter max_retreies 
It calls an the LLM API with the model name to request it to generate solution steps, and generate the corresponding 
Python code for the solution. It then calls the corresponding Python functions to solve the problem. 
If there is error in executing the Python code, it will re-prompt the LLM to re-generate the code with a 
fix to the error until a successful execution of the code or max retires has been exhausted

# Requirements
Before running solver.py, the following are required:
- install openai
- set the env var "OPENAI_API_KEY" to the openAI API key you have created

# Example:
python solver.py --model="gpt-4o-mini" --max_retries=1 --problem="Find the equation of the tangent line to the graph of y = x^3 at x = 1/2"
