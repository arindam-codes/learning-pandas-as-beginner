import pandas as pd 

df = pd.read_csv("pokemon.csv")
print(df.to_string()) # .to_string() for reading the whole data