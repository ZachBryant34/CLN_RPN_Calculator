
import re

class Calculator:

    def calculate(self, operation):
        
        stack = []
        for exp in operation.split(" "):
            if exp in ["+","-", "*", "/"]:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if exp == "+":
                    answer = operand1 + operand2
                if exp == "-":
                    answer = operand1 - operand2
                if exp == "*":
                    answer = operand1 * operand2
                if exp == "/":
                    answer = operand1 / operand2
                stack.append(answer)
            else:
                stack.append(float(exp))
        return stack.pop()


print("Launching the claculator.....")
calc = Calculator()
user_input = ""
while user_input not in ["exit", "quit", "q", "stop", "close"]:
    regex = re.search('[a-zA-Z]', user_input)
    if regex != None:
        print("Please write an expression.")
    user_input = input(">")
    output = calc.calculate(user_input)
    print(output)
print("Closing the calculator...")