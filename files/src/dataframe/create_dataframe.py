import pandas as pd
import numpy as np


def create_dataframe(path) -> pd.DataFrame:
  dw_guide = pd.read_csv("dwguide.csv")
  dw_guide_titles = np.unique(dw_guide['title'].apply(lambda title: title.split(':')[0]))

  all_episodes = pd.read_csv("all-detailsepisodes.csv")
  doctor = {}
  for episode in all_episodes.sort_values('title').to_numpy():
    doctor[episode[1]] = episode[3]

  imdb = pd.read_csv("imdb_details.csv")
  rating = {}
  season = {}
  votes = {}
  for episode in imdb.sort_values('title').to_numpy():
    rating[episode[1]] = episode[2]
    votes[episode[1]] = episode[3]
    season[episode[1]] = episode[5]

  clean_dataframe = {
    'title': [],
    'doctor': [],
    'rating': [],
    'votes': [],
    'season': []
  }
  for episode in dw_guide_titles:
    clean_dataframe['title'].append(episode)

    if episode in doctor:
      clean_dataframe['doctor'].append(doctor[episode])
    else:
      clean_dataframe['doctor'].append(None)

    if episode in rating:
      clean_dataframe['rating'].append(rating[episode])
      clean_dataframe['votes'].append(votes[episode])
      clean_dataframe['season'].append(season[episode])
    else:
      clean_dataframe['rating'].append(None)
      clean_dataframe['votes'].append(None)
      clean_dataframe['season'].append(None)

  clean_dataframe = pd.DataFrame(clean_dataframe)
  clean_dataframe.to_xml(path)
  return clean_dataframe


if __name__ == "__main__":
  print(create_dataframe('./dataframe.xml'))
