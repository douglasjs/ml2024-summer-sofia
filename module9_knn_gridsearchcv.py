import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class KNNClassifier:
    def __init__(self):
        self.train_X = None
        self.train_Y = None
        self.test_X = None
        self.test_Y = None

    def read_dataset(self, n, dataset_name):
        X = np.zeros(n)
        Y = np.zeros(n, dtype=int)

        for i in range(n):
            X[i] = float(input(f"Enter x value (feature) for {dataset_name} point {i + 1}: "))
            Y[i] = int(input(f"Enter y value (label) for {dataset_name} point {i + 1}: "))

            while Y[i] < 0:
                print("Y must be a non-negative integer. Please enter again.")
                Y[i] = int(input(f"Enter y value (label) for {dataset_name} point {i + 1}: "))

        return X.reshape(-1, 1), Y  # Reshape X for sklearn compatibility

    def input_data(self):
        trainingLabel = "Enter the number of training (x, y) pairs (N): "
        N = self.validate_input(int(input(trainingLabel)), trainingLabel)
        self.train_X, self.train_Y = self.read_dataset(N, "training")
        
        testLabel = "Enter the number of test (x, y) pairs (M): "
        M = self.validate_input(int(input(testLabel), testLabel))
        self.test_X, self.test_Y = self.read_dataset(M, "test")
        
    def validate_input(self, value, inputLabel):
        while value > 10:
            print("Invalid input. Please enter below 10.")
            value = int(input(inputLabel))
        return value

    def find_best_k(self):
        best_k = 1
        best_accuracy = 0.0

        for k in range(1, 11):
            if k > len(self.train_X):
                break
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(self.train_X, self.train_Y)

            # Predict the classes of the test set
            predicted_Y = knn.predict(self.test_X)

            # Calculate the accuracy
            accuracy = accuracy_score(self.test_Y, predicted_Y)
            print(f"Accuracy for k={k}: {accuracy:.2f}")

            # Update best k if the current k yields better accuracy
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_k = k

        return best_k, best_accuracy


def main():
    knn_classifier = KNNClassifier()
    knn_classifier.input_data()
    best_k, best_accuracy = knn_classifier.find_best_k()

    print(f"\nBest k: {best_k}")
    print(f"Test Accuracy for best k: {best_accuracy:.2f}")
    
if __name__ == "__main__":
    main()