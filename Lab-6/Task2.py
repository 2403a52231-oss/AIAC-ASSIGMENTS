def print_multiples_for(number):
    print("Using FOR loop:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}") 
def print_multiples_while(number):
    print("\nUsing WHILE loop:")
    i = 1
    while i <= 10:
        result = number * i
        print(f"{number} x {i} = {result}")
        i = i + 1
num = int(input("Enter Number to see its first 10 multiples: "))
print_multiples_for(num)
print_multiples_while(num)
    