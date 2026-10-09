import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sales_Analysis_Project.csv")


#DATA CLEANING & EDA 

print("Shape:")
print(df.shape)

print("\n Missing values:")
print(df.isnull().sum())

print("\n Duplicates Rows:")
print(df.duplicated().sum())

print("\n Data Types:")
print(df.dtypes)

print("\n Basic Statistics:")
print(df.describe())

#DATA CLEANING
# CONVERTING ORDER DATE COLUMN FROM STRING TO DATETYPE TYPE

df["order_date"] = pd.to_datetime(df["order_date"])
print("\n Update data types:")
print(df.dtypes)

#feature engineering / feature creation:
#Taking existing data and creating useful new columns that make analysis easier.

#ANALYSIS COLUMN

df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["month_name"] = df["order_date"].dt.month_name()

print("\n Updated Data:")
print(df.head())

#KEY SALES ANALYSIS
#these are KPI(KEY PERFORMANCE INDICATORS)

print("\nTOTAL SALES:")
print(df["sales"].sum())

print("\nTOTAL PROFIT:")
print(df["profit"].sum())

print("\nTotal Quantity Sold:")
print(df["quantity"].sum())

print("\nAverage Order Value:")
print(df["sales"].mean())

print("\nNumber of Orders:")
print(df["order_id"].nunique())

#single product performance

product_sales = df.groupby("product")["sales"].sum()
print(product_sales.sort_values(ascending= False))

#single product profit

product_profit = df.groupby("product")["profit"].sum()
print(product_profit.sort_values(ascending= False))

#sales by region

print("\nSales by Region:")

region_sales = df.groupby("region")["sales"].sum()

print(region_sales.sort_values(ascending=False))

#profit by region
print("\nProfit by Region:")

region_profit = df.groupby("region")["profit"].sum()

print(region_profit.sort_values(ascending=False))

#monthly sales
print("\nMonthly Sales:")

monthly_sales = df.groupby("month")["sales"].sum()

print(monthly_sales)

best_month = monthly_sales.idxmax()
worst_month = monthly_sales.idxmin()

print("\nBest Month:", best_month)
print("Best Month Sales:", monthly_sales.max())

print("\nWorst Month:", worst_month)
print("Worst Month Sales:", monthly_sales.min())

#MATPLOTLIB
import matplotlib.pyplot as plt

monthly_sales.plot(kind="bar")

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

print("\nTop 10 Customers by Sales:")

customer_sales = (
    df.groupby("customer_id")["sales"]
    .sum()
    .sort_values(ascending=False)
)

print(customer_sales.head(10))

#discount analysis

print("\nSales and Profit by Discount:")

discount_analysis = df.groupby("discount_pct").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
    total_orders=("order_id", "count")
)

print(discount_analysis)

discount_analysis["profit_margin_pct"] = (
    discount_analysis["total_profit"]/ discount_analysis["total_sales"])*100

print("\nDiscount Analysis with Profit Margin:")
print(discount_analysis.round(2))

discount_analysis[["total_sales", "total_profit"]].plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Sales and Profit by Discount")
plt.xlabel("Discount Percentage")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=0)
plt.legend(["Total Sales", "Total Profit"])
plt.tight_layout()
plt.show()

#summary

print("\n========== SALES ANALYSIS SUMMARY ==========")

print(f"Total Sales: ₹{df['sales'].sum():,.2f}")
print(f"Total Profit: ₹{df['profit'].sum():,.2f}")
print(f"Total Orders: {df['order_id'].nunique():,}")
print(f"Total Quantity Sold: {df['quantity'].sum():,}")

print(f"Best Sales Month: {monthly_sales.idxmax()}")
print(f"Best Month Sales: ₹{monthly_sales.max():,.2f}")

print(f"Lowest Sales Month: {monthly_sales.idxmin()}")
print(f"Lowest Month Sales: ₹{monthly_sales.min():,.2f}")

print(f"Top Product: {product_sales.idxmax()}")
print(f"Top Region by Sales: {region_sales.idxmax()}")
print(f"Top Region by Profit: {region_profit.idxmax()}")


# Regional Sales and Profit Analysis

regional_performance = df.groupby("region")[["sales", "profit"]].sum()

print("\nRegional Sales and Profit:")
print(regional_performance)

# Calculate Profit Margin by Region
regional_performance["profit_margin_pct"] = (
    regional_performance["profit"] /
    regional_performance["sales"]
) * 100

print("\nRegional Profit Margin:")
print(regional_performance[["profit_margin_pct"]].round(2))

# Create chart
regional_performance.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Regional Sales vs Profit")
plt.xlabel("Region")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.legend(["Sales", "Profit"])
plt.tight_layout()
plt.show()

# Category Performance Analysis

category_performance = df.groupby("category").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
    total_quantity=("quantity", "sum")
)

print("\nCategory Performance:")
print(category_performance.sort_values(
    by="total_sales", ascending=False
))

# Visualize category sales
category_performance["total_sales"].sort_values().plot(
    kind="barh",
    figsize=(10, 6)
)

plt.title("Sales by Product Category")
plt.xlabel("Total Sales")
plt.ylabel("Category")
plt.tight_layout()
plt.show()

# Product Profitability Analysis

product_profitability = df.groupby("product").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum")
)

product_profitability["profit_margin_pct"] = (
    product_profitability["total_profit"] /
    product_profitability["total_sales"]
) * 100

product_profitability = product_profitability.sort_values(
    by="profit_margin_pct",
    ascending=False
)

print("\nProduct Profitability Analysis:")
print(product_profitability.round(2))

# Visualize profit margins
product_profitability["profit_margin_pct"].plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Profit Margin by Product")
plt.xlabel("Product")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Customer Profit Analysis

customer_profit = df.groupby("customer_id").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum")
)

top_10_profit_customers = customer_profit.sort_values(
    by="total_profit",
    ascending=False
).head(10)

print("\nTop 10 Customers by Profit:")
print(top_10_profit_customers.round(2))

# Visualize top 10 customers by profit
top_10_profit_customers["total_profit"].sort_values().plot(
    kind="barh",
    figsize=(10, 6)
)

plt.title("Top 10 Customers by Profit")
plt.xlabel("Total Profit")
plt.ylabel("Customer ID")
plt.tight_layout()
plt.show()

df.to_csv("Sales_Analysis_Cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")

# Final Business Insights

best_region = regional_performance["profit_margin_pct"].idxmax()
best_product = product_profitability["profit_margin_pct"].idxmax()
best_customer = top_10_profit_customers["total_profit"].idxmax()
best_category = category_performance["total_sales"].idxmax()

print("\n========== FINAL BUSINESS INSIGHTS ==========")

print(f"Most Profitable Region by Margin: {best_region}")
print(f"Highest Margin Product: {best_product}")
print(f"Most Profitable Customer ID: {best_customer}")
print(f"Top Category by Sales: {best_category}")

print("\nRecommendations:")
print("1. Investigate why the lowest-margin region underperforms.")
print("2. Review pricing and costs for products with lower profit margins.")
print("3. Understand purchasing patterns of the most profitable customers.")
print("4. Use category-level sales trends to guide inventory planning.")