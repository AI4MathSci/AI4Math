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
```bash
- install openai
- set the env var "OPENAI_API_KEY" to the openAI API key you have created
```
# Example:
Run the following example to solve a math problem:
```bash
python solver.py --model="gpt-4o-mini" --max_retries=1 --problem="Find the equation of the tangent line to the graph of y = x^3 at x = 1/2"
```
You should expect an output similar to the following:

Generated Code:
========================================
```Python
# To find the equation of the tangent line to the graph of y = x^3 at x = 1/2, we will first calculate the derivative to find the slope of the tangent line at that point.

import sympy as sp

# Define the variable and function
x = sp.symbols('x')
y = x**3

# Calculate the derivative (slope of the tangent line)
dy_dx = sp.diff(y, x)

# Evaluate the slope at x = 1/2
slope_at_1_2 = dy_dx.subs(x, 1/2)

# Calculate the y-coordinate of the point on the curve at x = 1/2
y_at_1_2 = y.subs(x, 1/2)

# The equation of the tangent line in point-slope form is y - y1 = m(x - x1)
# Where (x1, y1) is the point of tangency and m is the slope
# Rearranging gives y = m(x - x1) + y1

tangent_line_eq = slope_at_1_2 * (x - 1/2) + y_at_1_2

# Print the slope and the equation of the tangent line
print(f"Slope of the tangent line at x = 1/2: {slope_at_1_2}")
print(f"Equation of the tangent line: {tangent_line_eq}")
```

========================================

Execution Output:
 Slope of the tangent line at x = 1/2: 0.750000000000000
Equation of the tangent line: 0.75*x - 0.25

Successfully executed the code.


