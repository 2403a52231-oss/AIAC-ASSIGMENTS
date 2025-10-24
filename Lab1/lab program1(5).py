with open('example.txt', 'w') as f:
    f.write('HELLO!!\n')
    f.write("THIS SUBJECT WAS AIAC.\n")
    f.write("BY USING PYTHON CODE.\n")
def count_lines_with_value(filename, value):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if value in line:
                count += 1
    return count

try:
    result = count_lines_with_value('example.txt', 'HELLO')
    print(result)
except FileNotFoundError:
    print("The file 'example.txt' was not found.")

