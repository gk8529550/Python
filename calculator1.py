def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def mod(x,y):
    return x%y
def exponentiation(x,y):
    return x**y
def floordivision(x,y):
    return x//y
print("Select operator:")
print("press 1 for add:")
print("prees 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for diivision")
print("press 5 for module")
print("press 6 for exponentiation")
print("press 7 for floor division")

while choice!=8:
    choice= input("enter(1/2/3/4/5/6/7):")
    if choice in('1','2','3','4','5','6','7'):
        try:
           num1=float("enter first value")
           num2=float("enter second value")
        except ValueError:
            print("invalid input,please i=enter valid input")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", mod(num1, num2))

        elif choice == '6':
            print(num1, "**", num2, "=", exponentiation(num1, num2))

        elif choice == '7':
            print(num1, "//", num2, "=", floordivision(num1, num2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
        