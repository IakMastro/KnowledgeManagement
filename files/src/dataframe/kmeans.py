import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.cluster import KMeans


# KMeans implementation
def kmeans(dataframe: pd.DataFrame) -> None:
  k_means = KMeans(n_clusters=4, init="k-means++", random_state=0).fit(dataframe)

  sns.scatterplot(data=dataframe, x="low", y="high", hue=k_means.labels_)
  plt.scatter(k_means.cluster_centers_[:, 0], k_means.cluster_centers_[:, 1], marker='X', c="r", s=80, label="centroids")
  plt.savefig('k_means_cluster.png')
  plt.show()
