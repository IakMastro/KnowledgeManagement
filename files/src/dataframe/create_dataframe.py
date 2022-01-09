import pandas as pd


# Clean dataset implementation
def create_dataframe(path, dataset_path='./forex.csv') -> pd.DataFrame:
  # Read data from the CSV source file
  dataset = pd.read_csv(dataset_path)
  dataset.to_xml(path)

  # Keep only the info that is needed
  dataset = dataset.where(dataset['currency'] == 'EUR').dropna()
  dataset = dataset.where(dataset['high'] < 2).dropna()
  dataset = dataset.where(dataset['high'] > 0.2).dropna()

  # Dictionary
  clean_dataset = {
    'high': dataset['high'],
    'low': dataset['low'],
    'open': dataset['open'],
    'close': dataset['close']
  }

  # Parse dictionary to new DataFrame, save it and return this back
  clean_dataset = pd.DataFrame(clean_dataset)
  clean_dataset.to_csv('./dataset.csv')
  return clean_dataset


if __name__ == "__main__":
  print(create_dataframe('./dataframe.xml'))
