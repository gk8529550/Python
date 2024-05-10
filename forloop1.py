def print_multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number to print its multiplication table: "))
        print_multiplication_table(user_input)
    except ValueError:
        print("Please enter a valid number.")
