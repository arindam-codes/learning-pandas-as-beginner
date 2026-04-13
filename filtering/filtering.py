import pandas as pd

df = pd.read_csv("../importing/pokemon.csv")

# Filtering rows that match a condition
# tall_pokemon = df[df["Height"] >= 2]
# print(tall_pokemon)

### inner df["Height"] >= 2 is checking every rows and giving a list of true false values
### the outer df[] just showing the true values

# # Heavy pokemon

# heavy_pokemon = df[df["Weight"] > 100]
# print(heavy_pokemon)

# # Legendary pokemon
# legendary_pokemon = df[df["Legendary"] == 1]
# print(legendary_pokemon)

# Water Pokemon
water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
print(water_pokemon)

## | -> or, & -> and
