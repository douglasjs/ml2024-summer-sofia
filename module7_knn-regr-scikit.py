import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNN:
    def __init__(self):
        self.model = None
        self.X_train = None
        self.y_train = None

    def read_data(self):
        self.N = int(input("Enter the number of points (N): "))
        if self.N <= 0:
            raise ValueError("N must be a positive integer.")

        self.k = int(input("Enter the value of k: "))
        if self.k <= 0:
            raise ValueError("k must be a positive integer.")

        if self.k > self.N:
            raise ValueError("k cannot be greater than N.")

        X = []
        y = []
        
        for i in range(self.N):
            x_value = float(input(f"Enter x value for point {i+1}: "))
            y_value = float(input(f"Enter y value for point {i+1}: "))
            X.append([x_value])
            y.append(y_value)
            
        self.X_train = np.array(X)
        self.y_train = np.array(y)

    def calculate_variance(self):
        if self.y_train is None:
            raise ValueError("Training data is not loaded.")
        return np.var(self.y_train)

    def train_model(self):
        if self.k > self.N:
            raise ValueError("k cannot be greater than N.")
        self.model = KNeighborsRegressor(n_neighbors=self.k)
        self.model.fit(self.X_train, self.y_train)

    def predict(self, X_pred):
        if self.model is None:
            raise ValueError("Model is not trained.")
        X_pred = np.array([[X_pred]])
        return self.model.predict(X_pred)[0]

def main():
    try:
        knn_regressor = KNN()
        knn_regressor.read_data()
        variance = knn_regressor.calculate_variance()
        print(f"Variance of labels in the training dataset: {variance}")
        
        knn_regressor.train_model()
        
        X_pred = float(input("Enter the value of X for prediction: "))
        y_pred = knn_regressor.predict(X_pred)
        print(f"Predicted Y value for X = {X_pred}: {y_pred}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()