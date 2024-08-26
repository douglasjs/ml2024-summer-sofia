from sklearn.metrics import precision_score, recall_score

class ClassificationMetrics:
    def __init__(self, n):
        self.n = n
        self.x_values = []
        self.y_values = []

    def add_point(self, x, y):
        self.x_values.append(x)
        self.y_values.append(y)

    def calculate_precision(self):
        return precision_score(self.x_values, self.y_values,labels=None, average='binary',)

    def calculate_recall(self):
        return recall_score(self.x_values, self.y_values,labels=None, average='binary',)
    
    def validate_input(self, value, inputLabel):
        while value not in [0, 1]:
            print("Invalid input. Please enter 0 or 1.")
            value = int(input(inputLabel))
        return value

def main():
    N = int(input("Enter the number of (x, y) points: "))
    metrics = ClassificationMetrics(N)

    for i in range(N):
        xInputLabel = f"Enter x value (ground truth) for point {i+1}: "
        x = metrics.validate_input(int(input(xInputLabel)), xInputLabel)
        yInputLabel = f"Enter y value (ground truth) for point {i+1}: "
        y = metrics.validate_input(int(input(yInputLabel)), yInputLabel)
        metrics.add_point(x, y)

    precision = metrics.calculate_precision()
    recall = metrics.calculate_recall()
    
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()