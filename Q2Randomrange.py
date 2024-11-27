import random

def generate_numbers():
    min_value = int(input("Enter the minimum value of the range: "))
    max_value = int(input("Enter the maximum value of the range: "))

    while max_value <= min_value:
        print("Invalid range. Maximum value should be greater than minimum value.")
        min_value = int(input("Enter the minimum value of the range: "))
        max_value = int(input("Enter the maximum value of the range: "))

    num1 = random.randint(min_value, max_value)
    num2 = random.randint(min_value, max_value)

    print(f"Generated numbers: {num1}, {num2}")

generate_numbers()
