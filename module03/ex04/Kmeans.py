import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# https://medium.com/analytics-vidhya/3d-visualization-of-k-means-clustering-47d3d3e82117

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.ncentroid = ncentroid # number of centroids
        self.centroids = [] # values of the centroids
        
    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -----
            None.
        Raises:
        -----
            This function should not raise any Exception.
        """
        # Randomly initialize centroids
        self.centroids = X[np.random.choice(X.shape[0], self.ncentroid, replace=False), :]
        print("Randomly initialized centroids: ", self.centroids)
        # Iterate until convergence
        while True:
            # Assign each data point to the nearest centroid
            labels = self._assign_centroids(X)
            
            # Update centroids based on the mean of assigned data points
            new_centroids = self._update_centroids(X, labels)
            
            # Check for convergence
            if np.allclose(new_centroids, self.centroids):
                break
            
            # Update centroids
            self.centroids = new_centroids
            
    def _assign_centroids(self, X):
        """
        Assign each data point to the nearest centroid.
        Args:
        -----
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -----
            labels: numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -----
            This function should not raise any Exception.
        """
        # Compute distance between each data point and each centroid
        distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)
        