import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.cluster import KMeans


# KMeans implementation
def kmeans(dataframe: pd.DataFrame, n_clusters=4, path: str = "k_means_cluster.png") -> None:
  k_means = KMeans(n_clusters=n_clusters, init="k-means++", random_state=0).fit(dataframe)

  sns.scatterplot(data=dataframe, x="low", y="high", hue=k_means.labels_)
  plt.scatter(k_means.cluster_centers_[:, 0], k_means.cluster_centers_[:, 1], marker='X', c="r", s=80, label="centroids")
  plt.savefig(path)
  plt.show()


if __name__ == '__main__':
  dataframe = pd.DataFrame({
    'high': [1, 2, 3, 4],
    'low': [2, 1, 4, 3]
  })

  kmeans(dataframe, 2, 'k_means_example.png')
