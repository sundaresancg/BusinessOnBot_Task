def calculate(expression):
    try:
        operands = expression.split()
        operator = operands.pop(1)
        a = float(operands[0])
        b = float(operands[1])
        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            result = a / b
        else:
            result = "Invalid operator"

        return result

    except:
        return "Invalid expression"

while True:
    print("~ Hello! I'm a calculator.")
    exp = input("~ Enter an expression (type 'exit' to quit)\n")
    if exp == 'exit':
        print("~ Goodbye!")
        break
    result = calculate(exp)
    print("Solution = ",result)
