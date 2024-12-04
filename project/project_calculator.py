import calculator_module as calc
while True:
    print("simple calculator\n")
    print("choose an option:")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.view History")
    print("6.exit")

    choice = input("enter what you want to do (1-6): ")

    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("enter a number between 1 and 6.\n")
        continue

    if choice in ['1', '2', '3', '4']:
        while True:
            try:
                num1 = float(input("enter the first number: "))
                num2 = float(input("enter the second number: "))
                break
            except ValueError:
                print("invalid input.\n")
        print(f"you entered: {num1} and {num2}")

        if choice == '1':
            result = calc.add(num1, num2)
            calc.history("+", num1, num2, result)
        elif choice == '2':
            result = calc.subtract(num1, num2)
            calc.history("-", num1, num2, result)
        elif choice == '3':
            result = calc.multiply(num1, num2)
            calc.history("*", num1, num2, result)
        elif choice == '4':
            if num2 == 0:
                result = "error"
            else:
                result = calc.divide(num1, num2)
                calc.history("/", num1, num2, result)
        print(f"result: {result}\n")

    elif choice == '5':
        calc.view_history()
    else:
        print("exit")
        break
