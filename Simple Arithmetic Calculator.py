def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Let\'s solve maths problem for you.")
print("For add, select '1' ")
print("For subtract, select '2' ")
print("For multiply, select '3' ")
print("For divide, select '4' ")

choice = input("Select either(1/2/3/4): ")


if choice in ('1', '2', '3', '4'):
    try:
        num1 = float(input('Choose a number: '))
        num2 = float(input('Choose a number: '))

    except ValueError:
        print('Invalid input. Please choose correctly.')

    if choice == '1':
        print(num1, '+', num2, '=', add(num1, num2))

    elif choice == '2':
        print(num1, '-', num2, '=', subtract(num1, num2))

    elif choice == '3':
        print(num1, '*', num2, '=', multiply(num1, num2))

    elif choice == '4':
        print(num1, '/', num2, '=', divide(num1, num2))

    new_calculation = input("Let\'s do another calculation (yes/no): ")
    if new_calculation == "no":
        print("Thanks for using the calculator!")

    else:
        print("Please rerun the code to start all over again")

else:
    print("Invalid input. Please try again and choose the correct option")
