from sklearn.metrics import precision_score, recall_score
from collections import deque
import numpy as np

class ClassificationMetrics:
    def __init__(self, n):
        self.n = n
        self.x_values = deque(maxlen=n)
        self.y_values = deque(maxlen=n)

    def add_point(self, x, y):
        self.x_values.append(x)
        self.y_values.append(y)

    def npArray(self):
        x_array = np.array(self.x_values)
        y_array = np.array(self.y_values)
        return x_array, y_array
    
    def calculate_recall(self):
        coverDequeToArrayX, coverDequeToArrayY = self.npArray()
        return recall_score(coverDequeToArrayX, coverDequeToArrayY,labels=None, average='binary',)

    def calculate_precision(self):
        coverDequeToArrayX, coverDequeToArrayY = self.npArray()
        return precision_score(coverDequeToArrayX, coverDequeToArrayY,labels=None, average='binary',)

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