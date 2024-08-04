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