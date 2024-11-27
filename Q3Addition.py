import random
def hello_there():
    min_value = 1
    max_value = 100
    num1 = random.randint(min_value, max_value)
    num2 = random.randint(min_value, max_value)
    print(num1, '+', num2)
    a = int(input())
    if a == num1 + num2:
        print('Good job')
    else:
        print('So uncivilized')
hello_there()
