# Create a list of numbers and find their average.

value = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

total = 0
for v in value:
    total += v

average = total / len(value)

print("The average is:", average)
