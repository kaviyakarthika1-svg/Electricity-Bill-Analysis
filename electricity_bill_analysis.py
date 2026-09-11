import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Electricity_bill.csv")

print("First 5 Rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInformation:")
df.info()

print("\nDescription:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

df["Bill"] = df["Units_Consumed"] * 5

print("\nAverage Bill:")
print(df["Bill"].mean())

print("\nHighest Bill:")
print(df["Bill"].max())

print("\nLowest Bill:")
print(df["Bill"].min())

plt.figure(figsize=(6,4))
plt.hist(df["Bill"])
plt.title("Bill Amount Distribution")
plt.xlabel("Bill Amount")
plt.ylabel("Number of Customers")
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(df["Units_Consumed"], df["Bill"])
plt.title("Units Consumed vs Bill")
plt.xlabel("Units Consumed")
plt.ylabel("Bill Amount")
plt.show()

plt.figure(figsize=(6,4))
df.groupby("City")["Bill"].mean().plot(kind="bar")
plt.title("Average Bill by City")
plt.xlabel("City")
plt.ylabel("Average Bill")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(y=df["Bill"])
plt.title("Bill Amount Box Plot")
plt.show()

plt.figure(figsize=(7,5))
sns.heatmap(df.select_dtypes("number").corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show