def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

try:
    num = int(input("Enter the value of n: "))
    print(f"The {num}th Fibonacci number is: {fibonacci(num)}")
except ValueError:
    print("Please enter a valid integer.")



    
