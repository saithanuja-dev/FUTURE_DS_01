import os
import pandas as pd
import matplotlib.pyplot as plt


os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("train.csv")


print("TOTAL REVENUE")
print(df["Sales"].sum())


category_sales = df.groupby("Category")["Sales"].sum()
region_sales = df.groupby("Region")["Sales"].sum()


plt.figure(figsize=(6,4))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig("category_sales.png")   # SAVE FIRST
plt.close()


plt.figure(figsize=(6,4))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig("region_sales.png")     # SAVE FIRST
plt.close()