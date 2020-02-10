from sklearn import cluster
import pandas as pd
import numpy as np



dataset = pd.DataFrame({
    'x': [11, 11, 20, 12, 16, 33, 24, 14, 45, 52, 51, 52, 55, 53, 55, 61, 62, 70, 72, 10],
    'y': [39, 36, 30, 52, 53, 46, 55, 59, 12, 15, 16, 18, 11, 23, 14, 8, 18, 7, 24, 70]
})

myKmeans = cluster.KMeans(n_clusters=2)
myKmeans.fit(dataset)

labels = myKmeans.labels_
print(labels)


centroids = k_means.cluster_centers_
print(centroids)
centroids[0]

import matplotlib.pyplot as plt

dataset['x']


plt.scatter(dataset['x'],dataset['y'], s=10)
plt.scatter(centroids[0],centroids[1],s=100)
plt.show()



