import math
# Menu base calculator:

def Menu():
    print("\n------ Scientific Calculator -------")
    print("Select opration: ")
    print("1- Addition")
    print("2- Subtraction")
    print("3- Multiplication")
    print("4 - Division")
    print("5- Exponent")
    print("6- Square root")
    print("7 - Factorial")
    print("8 - Natural logarithm")
    print("9 - Logarithm with base 10")
    print("10 - Sine")
    print("11 - Cosine")
    print("12 - Tangent")
    print("13 - Exit")



def Add(a, b):
    return a + b

def Sub(a, b):
    return a - b

def Mul(a, b):
    return a * b

def Div(a, b): 

    if b != 0:
        return a / b 
    else:
        return "Error, Division by zero!"

def Power(a, b):
    return a ** b

def square_root(num):
    if num >= 0:
        return math.sqrt(number)
    else:
        return "Error, Square root of negative number!"
def Factorial(num):
    if num >= 0:
        return math.factorial(int(num))
    else:
        return "Error, Factorial requires non negative number."

def Natura_log(num):
    if num > 0:
        return math.log(num)
    else:
        return "Error, logarithm requires positive number."

def Log_wiht_base_ten(num):
    if num > 0:
        return math.log10(num)
    else:
        return "Error, logarithm requires a positive number."

def Sine(num):
    return math.sin(math.radians(num))

def Cosine(num):
    return math.cos(math.radians(num))

def Tangent(num):
    if num % 180 == 90:
        return "Error, Tangent is undefined at this angle."
    else:
        return math.tan(math.radians(num))

def Exit():
    print("Exiting calculator. Goodbye!")



         

while True:
    Menu()
    try:


        choice = int(input("Choose option: "))

    except ValueError:
        print("Invalid input! Please choose options 1 to 4.")
        continue

    if choice == 13:
        Exit()
        break

    # operatons that needs two numbers
    if choice in [1, 2, 3, 4, 5]:

        try:

         num_one = float(input("Enter first number: "))
         num_two = float(input("Enter second number: "))

        except ValueError:
            print("Invalid input! Please enter only numbers.")
            continue

    # operations that needs solely one number.
    if choice in [6, 7, 8, 9, 10, 11, 12]:

        try:

            number = float(input("Enter a number: "))

        except ValueError:
            print("Error, Please enter only numbers.")
            continue


        if choice == 1:
            print("Result: ", Add(num_one, num_two))

        elif choice == 2:
            print("Result: ", Sub(num_one, num_two))

        elif choice == 3:
            print("Result: ", Mul(num_one, num_two))

        elif choice == 4:
            print("Result: ", Div(num_one, num_two))

        elif choice == 5:
                print("Result: ", Power(num_one, num_two))

        elif choice == 6:
            print("Result: ", square_root(number))

        elif choice == 7:
            print("Result: ", Factorial(number))

        elif choice == 8:
            print("Result: ", Natura_log(number))

        elif choice == 9:
            print("Result: ", Log_wiht_base_ten(number))

        elif choice == 10:
            print("Result: ", Sine(number))

        elif choice == 11:
            print("Result: ", Cosine(number))

        elif choice == 12:
            print("Result: ", Tangent(number))

        else:
            print("Invalid input!")

        Perform_again = input("Do you want to perform another calculation? (yes/no)").lower()
        if Perform_again != "yes":
            print("Thank You!")
            break