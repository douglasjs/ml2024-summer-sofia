import numpy as np

class KNN:
    def __init__(self, k):
        self.k = k
        self.points = np.array([])

    def insert_data(self, x, y):
        if self.points.size == 0:
            self.points = np.array([[x, y]])
        else:
            self.points = np.vstack([self.points, [x, y]])

    def predict(self, x):
        if self.points.shape[0] < self.k:
            return "Error: k cannot be greater than the number of available points."
        print(self.points)
        # Manhattan distance
        distances = np.abs(self.points[:, 0] - x)
        # Sort by distance and get indices of k nearest neighbors
        nearest_neighbors_indices = np.argsort(distances)[:self.k]
        # Return the mean of the y values of the nearest neighbors
        return int(np.mean(self.points[nearest_neighbors_indices, 1]))

def main():
    N = int(input("Enter the number of points (N): "))
    k = int(input("Enter the number of nearest neighbors (k): "))
    
    knn_regressor = KNN(k)
    
    for i in range(N):
        x = float(input(f"Enter x value for point {i+1}: "))
        y = float(input(f"Enter y value for point {i+1}: "))
        knn_regressor.insert_data(x, y)
    
    x_valueInput = float(input("Enter the x value for prediction: "))
    result = knn_regressor.predict(x_valueInput)
    print("Predicted y value:", result)

if __name__ == "__main__":
    main()