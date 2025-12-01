import sys


def cal(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        else:
            return num1 / num2
    else:
        raise ValueError("Unknown operator")


memory = None

while True:

    while True:
        prompt = "Enter first number"
        if memory is not None:
            prompt += f" (or 'm' for {memory})"

        user_input = input(f"{prompt} or 'q' to quit: ").strip().lower()

        if user_input == "q":
            print("Goodbye!")
            sys.exit()

        if user_input == "m":
            if memory is None:
                print("Error: Memory is empty. Please enter a number.")
                continue
            else:
                num1 = memory
                print(f"Using memory: {num1}")
                break
        else:
            try:
                num1 = float(user_input)
                break
            except ValueError:
                print("Invalid input! Please enter a number.")

    while True:
        op_input = input("Enter operator (+, -, *, /): ").strip().lower()

        if op_input == "q":
            print("Goodbye!")
            sys.exit()

        if op_input in ["+", "-", "*", "/"]:
            op = op_input
            break
        else:
            print("Invalid operator! Please enter +, -, *, or /")

    while True:
        user_input = input("Enter second number: ").strip().lower()

        if user_input == "q":
            print("Goodbye!")
            sys.exit()

        try:
            num2 = float(user_input)
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    try:
        result = cal(num1, op, num2)
        if result.is_integer():
            result = int(result)

        print(f"Result: {num1} {op} {num2} = {result}")

        memory = result

    except ValueError as e:
        print(f"Error: {e}")
