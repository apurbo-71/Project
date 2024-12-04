def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error"
    return a / b

calculation_history = []

def history(operation, a, b, result):
    calculation_history.append(f"{a} {operation} {b} = {result}")

def view_history():
    if not calculation_history:
        print("no history available\n")
    else:
        print("\ncalculation History:")
        for entry in calculation_history:
            print(entry)
