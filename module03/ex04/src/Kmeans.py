import numpy as np
import sys
import argparse
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
        indices = np.random.choice(X.shape[0], size=self.ncentroid, replace=False)
        self.centroids = X[indices]
        print("Randomly initialized centroids: ", self.centroids)
        # Iterate until convergence or max iterations reached
        for _ in range(self.max_iter):
            # Assign each data point to the nearest centroid
            labels = self._assign_labels(X)
            
            # Update centroids based on the mean of assigned data points
            self._update_centroids(X, labels)
            
    def predict(self, X):
        """
        Predict from which cluster each datapoint belongs to.
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
        labels = self._assign_labels(X)
        return labels
    
    def _assign_labels(self, X):
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
    
    def _update_centroids(self, X, labels):
        for i in range(self.ncentroid):
            self.centroids[i] = np.mean(X[labels == i], axis=0)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path to the dataset file')
    parser.add_argument('ncentroid', help='Number of centroids')
    parser.add_argument('max_iter', help='Maximum number of iterations')

    args = parser.parse_args()
    
    # Extract the values and convert them to the appropriate data type
    filepath = args.filepath.split('=')[1] if args.filepath else None
    ncentroid = args.ncentroid.split('=')[1] if args.ncentroid else None
    max_iter = args.max_iter.split('=')[1] if args.max_iter else None
    print("Filepath: ", filepath)
    print("Number of centroids: ", ncentroid)
    print("Maximum number of iterations: ", max_iter)
    return filepath, int(ncentroid), int(max_iter)

def read_dataset(filepath):
    try:
        # Read the dataset from the filepath
        data = np.genfromtxt(filepath, delimiter=",", skip_header=1)
        # Extract the feathures (height, weight, bone_density)
        X = data[:, 1:]
        return X
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        return None
        
def visualize_clusters(X, labels, centroids):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Assign colors to clusters
    colors = ['red', 'green', 'blue', 'yellow']
    # Plot data points
    for label in np.unique(labels):
        cluster_points = X[labels == label]
        ax.scatter(cluster_points[:, 0], cluster_points[:, 1], cluster_points[:, 2], c=colors[label], label=f"Cluster {label + 1}")
        
    # Plot centroids
    for i, centroid in enumerate(centroids):
        ax.scatter(centroid[0], centroid[1], centroid[2], c=colors[i], marker='o', s=100, label=f'Centroid {i + 1}')

    # Set labels and title
    ax.set_xlabel('Height')
    ax.set_ylabel('Weight')
    ax.set_zlabel('Bone Density')
    ax.set_title('Finding Homelands Results')
    
    # Add legend
    ax.legend()
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Parse the arguments
    filepath, ncentroid, max_iter = parse_arguments()
    
    if filepath is None:
        print("Error: Filepath is None")
        sys.exit(1)
    elif ncentroid is None:
        print("Error: ncentroid is None")
        sys.exit(1)
    elif max_iter is None:
        print("Error: max_iter is None")
        sys.exit(1)
        
    # Read the dataset
    data = read_dataset(filepath)
    
    if data is None:
        sys.exit(1)
        
    # Instantiate the class
    kmeans = KmeansClustering(max_iter=30, ncentroid=4)
    
    # Fit the data to perform clustering
    kmeans.fit(data)
    
    # Predict the cluster labels
    labels = kmeans.predict(data)
    
    # Visualize the clusters
    visualize_clusters(data, labels, kmeans.centroids)
         