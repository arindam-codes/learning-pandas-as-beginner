import pandas as pd

data = {
    "Name": ["kda", "avery", "brother"],
    "Age": [22, 19, 50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])
# print(df.loc["Employee 1"])
# print(df.iloc[1])

## Adding a new coloumn
df["Job"] = ["Engineer", "Cyber", "N/A"]
print(df)

## Adding  new rows 
new_row = pd.DataFrame([{"Name" : "Andu", "Age" : 60, "Job": "Jobless" },
                        {"Name" : "Pandu", "Age" : 70, "Job": "Jobless"}], 
                        index=["Employee 4", "Employee 5"])

df = pd.concat([df, new_row])


print(df)
