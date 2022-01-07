import pandas as pd

from dataframe.create_dataframe import create_dataframe
from dataframe.kmeans import kmeans
from dataframe.mean_shift import mean_shift
from os import path


if __name__ == '__main__':
  # Read dataset if exists, else clean the dataset and create a new one
  if path.isfile("./dataset.csv"):
    dataframe = pd.read_csv('./dataset.csv')
    dataframe.drop(dataframe.columns[[0]], axis=1, inplace=True)
  else:
    dataframe = create_dataframe('./dataframe.xml')

  # Print Dataframe info and print the content
  print("Dataframe info")
  dataframe.info()
  print(dataframe)

  # Run the Clustering algorithms
  kmeans(dataframe)
  mean_shift(dataframe)
