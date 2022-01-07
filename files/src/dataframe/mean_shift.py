import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.cluster import MeanShift, estimate_bandwidth


# MeanShift implementation
def mean_shift(dataframe: pd.DataFrame) -> None:
  bandwidth = estimate_bandwidth(dataframe, quantile=0.1, n_samples=100)
  clusters = MeanShift(bandwidth=bandwidth, bin_seeding=True).fit(dataframe)

  sns.scatterplot(data=dataframe, x="low", y="high", hue=clusters.labels_)
  plt.scatter(clusters.cluster_centers_[:, 0], clusters.cluster_centers_[:, 1], marker='x', c="r", s=80, label="centroids")
  plt.savefig('mean_shift_cluster.png')
  plt.show()