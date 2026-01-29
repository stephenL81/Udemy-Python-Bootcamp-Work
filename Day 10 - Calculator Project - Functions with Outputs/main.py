from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

print(logo)
total = 0
loop = True
carry_on = False

while loop:
    if carry_on == False:
        first_number = float(input("What is the first number? >>> "))
    print("+\n-\n*\n/")
    operation = input("Pick an operation >>> ")
    second_number = float(input("What's the next number? >>> "))

    my_addition = add
    my_subtraction = subtract
    my_multiplication = multiply
    my_division = divide

    operators = {
        "+":my_addition,
        "-":subtract,
        "*":multiply,
        "/":divide,
    }

    total = operators[operation](first_number,second_number)

    print(f"{first_number} {operation} {second_number} = {total}")
    if input(f"Type 'y' to continue calculating with {total} or type 'n' to start a new calculation >>>") == "n":
        total = 0
        carry_on = False
        print("\n"*20)
        print(logo)

    else:
        carry_on = True
        first_number = total


#Below is the official solution where recursion is used.

# import art
#
#
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }
#
# # print(operations["*"](4, 8))
#
#
# def calculator():
#     print(art.logo)
#     should_accumulate = True
#     num1 = float(input("What is the first number?: "))
#
#     while should_accumulate:
#         for symbol in operations:
#             print(symbol)
#         operation_symbol = input("Pick an operation: ")
#         num2 = float(input("What is the next number?: "))
#         answer = operations[operation_symbol](num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
#
#         choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
#
#         if choice == "y":
#             num1 = answer
#         else:
#             should_accumulate = False
#             print("\n" * 20)
#             calculator()
#
#
# calculator()