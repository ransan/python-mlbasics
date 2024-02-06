import pandas as pd


staff = pd.read_csv("src/data/staff.csv")
print(staff.head())
print(staff["name"].str[0:3])
print(staff["name"].str[-3:])
print(staff["name"].str[1::2])

for e in range(0, 10, 2):
    print(e)