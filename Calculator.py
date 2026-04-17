# Use ANSI styling for project title
print("\033[0;30;45m == BASIC CALCULATOR == \033[0m")

# Create function to check for decimal points
def input_number(prompt):
    while True:
        value = input(prompt)

        # Check for decimal/comma usage
        if "," in value:
            print("⚠️ Use a dot (.) instead of a comma (,)")
            continue
        try:
            return float(value)
        except ValueError:
            print("\033[2;34;40m Input must be a number! \033[0m")

# Operator List
operator_choice = None
while operator_choice != 0:
    print("\n Select Operator ")
    print("1. ➕ Addition")
    print("2. ➖ Substraction")
    print("3. ✖ Multiplication")
    print("4. ➗ Division")
    print("0. Exit")

    # Select an operator
    try:
        operator_choice = int(input("Select Operator (1/2/3/4/0) : "))
    except ValueError:
        print("\033[2;34;40m Input must be a number! \033[0m")
        continue

    if operator_choice == 0:
        print("\n 🤝 Thank You")
        break
    elif operator_choice not in [1, 2, 3, 4]:
        print("\033[2;34;40m Operator not found. Please try again! \033[0m")
        continue

    # Input
    A1 = input_number("Enter first number : ")
    A2 = input_number("Enter second number : ")

    # Calculation logic
    if operator_choice == 1:
        result = A1 + A2
        symbol = "+"
    elif operator_choice == 2:
        result = A1 - A2
        symbol = "-"
    elif operator_choice == 3:
        result = A1 * A2
        symbol = "x"
    elif operator_choice == 4:
        if A2 != 0:
            result = A1 / A2
            symbol = "/"
        else:
            result = "Undefined (Division by Zero)"
            symbol = "/"

    # Resukt
    print("\n", "="*8, "RESULT", "="*8)
    print(f"{A1} {symbol} {A2} = {result}")
