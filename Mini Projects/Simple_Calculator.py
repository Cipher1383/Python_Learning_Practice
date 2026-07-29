# Simple Calculator
def addition(num1, num2):
    return num1 + num2


def substraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def get_numbers():
    add_num1 = int(input("Enter the First Number:"))
    add_num2 = int(input("Enter the Second Number:"))
    return add_num1, add_num2


print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

usr_choice = int(input("Please choose an Operation of your choice from Above Options: "))
while usr_choice not in [1, 2, 3, 4]:
    print("Invalid Choice")
    usr_choice = int(input("Please choose an Operation of your choice from Above Options: "))

if usr_choice == 1:
    print("You have chosen Addition")
    add_num1, add_num2 = get_numbers()
    print(f'Addition of {add_num1} and {add_num2} is {addition(add_num1, add_num2)}')

elif usr_choice == 2:
    print("You have chosen Subtraction")
    add_num1, add_num2 = get_numbers()
    print(f'Substraction of {add_num1} and {add_num2} is {substraction(add_num1, add_num2)}')

elif usr_choice == 3:
    print("You have chosen Multiplication")
    add_num1, add_num2 = get_numbers()
    print(f'Multiplication of {add_num1} and {add_num2} is {multiplication(add_num1, add_num2)}')

elif usr_choice == 4:
    print("You have chosen Division")
    add_num1, add_num2 = get_numbers()
    print(f'Division of {add_num1} and {add_num2} is {division(add_num1, add_num2)}')
