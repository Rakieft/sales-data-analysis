import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/sales_data.csv")

# Convert Order Date from text to an actual date so we can group by day of week
df["Order Date"] = pd.to_datetime(df["Order Date"])

# --- Question 1: Which product category has the highest total sales? ---
revenue_by_category = df.groupby("Item Type")["Total Revenue"].sum().sort_values(ascending=False)
top_category = revenue_by_category.index[0]
top_category_revenue = revenue_by_category.iloc[0]

print("Question 1: Which product category has the highest total sales?")
print(revenue_by_category)
print(f"Answer: {top_category} has the highest total sales, with ${top_category_revenue:,.2f} in revenue.\n")

# --- Question 2: Which day of the week has the highest number of sales transactions? ---
df["Order Day"] = df["Order Date"].dt.day_name()
orders_by_day = df["Order Day"].value_counts()
top_day = orders_by_day.index[0]
top_day_count = orders_by_day.iloc[0]

print("Question 2: Which day of the week has the highest number of sales transactions?")
print(orders_by_day)
print(f"Answer: {top_day} has the most orders, with {top_day_count} transactions.\n")

# --- Graph: Total revenue by product category ---
plt.figure(figsize=(10, 6))
revenue_by_category.plot(kind="bar", color="steelblue")
plt.title("Total Revenue by Product Category")
plt.xlabel("Item Type")
plt.ylabel("Total Revenue ($)")
plt.tight_layout()
plt.savefig("revenue_by_category.png")
print("Graph saved as revenue_by_category.png")
