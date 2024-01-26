import numpy as np
import pandas as pd
import array

series = pd.Series([1,2,3], index=["a", "b", "c"])
print(series["a"])

dataFrame = pd.DataFrame({ "namee":["Ranjith", "Keerthi", "Chennai"], "age":["28", "29", "300"]})
print(dataFrame)

print("+++++++++++++++++++++++++++++++++++++++")

salesDataFrame = pd.read_csv("src/data/sales.csv", nrows=10)
print("head is : ")
print(salesDataFrame.head())

array_d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arrayPd = pd.DataFrame(array_d, columns=["A","B","C"])
print(arrayPd)
print("shape: ")
print(arrayPd.shape)
print("size: ")
print(arrayPd.size)
print("len: ")
print(len(arrayPd))

print("unique is : ")
print(salesDataFrame["product_group"].unique)
print(salesDataFrame["product_group"].nunique)

print(salesDataFrame["product_group"].value_counts())

print("mostFrequent : ")
print(salesDataFrame["product_group"].mode())

print("=======DataFrame Chanllange==========")

chanllange_dataframe_1 = pd.read_csv("src/data/sales.csv")
print(chanllange_dataframe_1["last_week_sales"].value_counts().nlargest(3).keys())

print("=====Challange 1 =======")
last_week_sales_count = list(chanllange_dataframe_1["last_week_sales"].value_counts().nlargest(3).index.values)
print(last_week_sales_count)


print("filtering  data")
salesfilter = salesDataFrame[(salesDataFrame["price"] > 100) & (salesDataFrame["last_week_sales"] >= 15 )]
print(salesfilter)


print("=====Challange 2 =======")
dataframe_challenge_2 = pd.read_csv("src/data/sales.csv")
avgprice = dataframe_challenge_2["price"].mean()
above_average_price = dataframe_challenge_2.query("price > @avgprice")
no_product_codes = above_average_price["product_code"].nunique()
print(no_product_codes)





