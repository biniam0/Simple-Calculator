import math


def main():
    print("Welcome to Simple Calculator")

    while True:
        section = input(
            "For Trigonometry press 'T' or Arithmetics press \'A\': ")
        if section == "T":
            try:
                trig = input("Enter the trig(sin, cos or tan): ")
                value_deg = float(input("The value in radian: "))

                value_rad = math.radians(value_deg)
                if trig == "sin":
                    result = math.sin(value_rad)
                elif trig == "cos":
                    result = math.cos(value_rad)
                elif trig == "tan":
                    result = math.tan(value_rad)
                else:
                    print("Invalid Trig")
                    continue
                print("Result: ", result)
            except ValueError:
                print("Invalic input. Please enter numeric values.")

        else:
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

                print("Result: ", result)
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
