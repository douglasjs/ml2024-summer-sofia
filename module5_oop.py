class NumberList:
    def __init__(self):
        self.numbers = []

    def initialize_data(self, count):
        self.numbers = []
        for i in range(count):
            num = int(input(f"Enter the number {i+1}: "))
            self.numbers.append(num)

    def insert_data(self, number):
        self.numbers.append(number)

    def search_data(self, X):
        indices = [i + 1 for i, num in enumerate(self.numbers) if num == X]
        return indices if indices else [-1]

def main():
    number_list = NumberList()

    # Data initialization
    count = int(input("How many positive integers will you input? "))
    number_list.initialize_data(count)

    # Data search
    X = int(input("Enter an integer X to check if it matches your provided numbers: "))
    result = number_list.search_data(X)

    # Output results
    if result != [-1]:
        if len(result) == 1:
            print("The index of matching X:", result[0])
        else:
            print("The indices of matching X:", result)
    else:
        print(-1)

if __name__ == "__main__":
    main()