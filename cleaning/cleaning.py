import pandas as pd

df = pd.read_csv("../importing/pokemon.csv")

# # Dropping irrelevant columns
# # df = df.drop(columns=["Legendary", "No"])
# # print(df)

# # Dropping missing data
# # df = df.dropna(subset=["Type2"]) # na means not available
# # print(df.to_string())

# # df = df.fillna({"Type2": "None"})
# # print(df.to_string())

# # Fixing inconsistent values
# # df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
# #                                   "Fire": "FIRE",
# #                                   "Water": "WATER"})
# # print(df.to_string())

# #  Standardize text
# # df["Name"] = df["Name"].str.lower

# # Fixing data types
# df["Legendary"] = df["Legendary"].astype(bool)

# print(df.to_string())

# ## Drop Duplicates
# df = df.drop_duplicates()
# print(df.to_string())