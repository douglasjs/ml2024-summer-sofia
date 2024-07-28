# ask user to input N number
number = int(input("How many positive integer will you input? "))

# Create empty array to store the numbers
numbers = []

# Ask the user to provide number one by one and read all of them
for i in range(number):
    num = int(input(f"Enter the number {i+1}: "))
    numbers.append(num)

# Ask the user to input X 
X = int(input("Enter an integer X to check if match you provided numbers: "))

# Find all index of X in the numbers array
indices = [i + 1 for i, num in enumerate(numbers) if num == X]

# check if X match the list of numbers
if X in numbers:
    # Output the index of matching numbers
    if len(indices) == 1:
        print("The index of matching X: ", indices[0])
    else:
        print("The indices of matching X: ", indices)
else:
    # Output -1 if there is not matching 
    print(-1)