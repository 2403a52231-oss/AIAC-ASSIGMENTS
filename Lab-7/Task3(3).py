with open("input.txt", "r") as data:
    lines = data.readlines()
with open("output.txt", "w") as output:
    for line in lines:
        output.write(line.upper())
print("Processing done")


