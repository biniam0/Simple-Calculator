def main():
    print("Welcome to Simple Calculator")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operation = input("Enter the operator: ")
            num2 = float(input("Enter the second number: "))
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2
            else:
                print("Invalid operation")
                continue

            print(result)
        except ValueError:
            print("Invalic input. Please enter numeric values.")
        except ZeroDivisionError:
            print("Division by Zero is not possible")
        answer = input(
            "Do you want to perform another calculation? (yes/no): ")
        if answer.lower() != "yes":
            break


if __name__ == "__main__":
    main()
