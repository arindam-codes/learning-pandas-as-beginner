import pandas as pd

df = pd.read_csv("importing/pokemon.csv", index_col="Name")

## Selection by coloumn
# print(df["Name"].to_string())
# print(df["Height"])
# print(df[["Name", "Height", "Weight"]])

## Selection by rows
# print(df.loc["Charizard" : "Blastoise", ["Height", "Weight"]])

# print(df.iloc[0:10:2, 0:3])

pokemon = input("Enter a pokemon name: ")

try:
    print(df.loc[pokemon])

except KeyError:
    print(f"{pokemon} not found")