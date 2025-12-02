def calculate(a, b, operation):
    a = float(a)
    b = float(b)
    operation = operation.lower()

    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error"
        return a / b
    else:
        return "Invalid"

a=int(input("a:"))
b=int(input("b:"))
f=str(input("Function:"))
print(calculate(a,b,f))