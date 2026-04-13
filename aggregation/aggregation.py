import pandas as pd

df = pd.read_csv("../importing/pokemon.csv")

# print(df.mean(numeric_only=True)) 
# print(df.min(numeric_only=True)) 
# print(df.max(numeric_only=True)) 
# print(df.count()) 

## Single Column
# print(df["Height"].mean()) 
# print(df["Height"].sum()) 
# print(df["Height"].max())  
# print(df["Height"].count()) 

grp = df.groupby("Type1")

# print(grp["Height"].mean())
print(grp["Height"].count())