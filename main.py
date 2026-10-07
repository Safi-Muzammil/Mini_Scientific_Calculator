
# Menu base calculator:

def Menu():
    print("\n------ Scientific Calculator -------")
    print("Select opration: ")
    print("1- Addition")
    print("2- Subtraction")
    print("3- Multiplication")
    print("4 - Division")



def Add(a, b):
    return a + b

def Sub(a, b):
    return a - b

def Mul(a, b):
    return a * b

def Div(a, b):
    return a / b





while True:
    Menu()

    choice = int(input("Choose option: "))

    num_one = float(input("Enter first number: "))
    num_two = float(input("Enter second number: "))

    if choice == 1:
        print("Result: ", Add(num_one, num_two))

    elif choice == 2:
        print("Result: ", Sub(num_one, num_two))

    elif choice == 3:
        print("Result: ", Mul(num_one, num_two))

    elif choice == 5:
        print("Result: ", Div(num_one, num_two))

    else:
        print("Invalid input!")
        break