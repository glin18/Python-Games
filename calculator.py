logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


should_continue = True
choice = 'n'

while should_continue:
    if choice == 'y':
        number = result
    else:
        number = float(input("What's the first number?: "))
    print("+ \n- \n* \n/")
    operation = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))

    if operation == "+":
        result = add(number, next_number)
    if operation == "-":
        result = subtract(number, next_number)
    if operation == "*":
        result = multiply(number, next_number)
    if operation == "/":
        result = divide(number, next_number)

    print(f"{number} {operation} {next_number} = {result} ")
    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 'q' "
                   f"to quit: ")
    if choice == 'q':
        should_continue = False

print("Thank you, see you next time")
