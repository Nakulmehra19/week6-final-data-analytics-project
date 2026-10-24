import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set project paths
DATA_PATH = "data/Sample - Superstore-Cleaned.xlsx"
OUTPUT_DIR = "visualizations"

# Create output folder if it does not exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Set visualization style
sns.set_theme(style="whitegrid")

# Load cleaned dataset
df = pd.read_excel(DATA_PATH)

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)


# 1. Sales by Category
plt.figure(figsize=(8, 5))
df.groupby("Category")["Sales"].sum().sort_values().plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "sales_by_category.png"))
plt.close()


# 2. Sales by Region
plt.figure(figsize=(8, 5))
df.groupby("Region")["Sales"].sum().sort_values().plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "sales_by_region.png"))
plt.close()


# 3. Monthly Sales Trend
monthly_sales = (
    df.dropna(subset=["Order Date"])
      .set_index("Order Date")["Sales"]
      .resample("MS")
      .sum()
)

plt.figure(figsize=(12, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "monthly_sales_trend.png"))
plt.close()


# 4. Correlation Heatmap
numeric_columns = ["Sales", "Profit", "Quantity", "Discount"]
correlation = df[numeric_columns].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "correlation_heatmap.png"))
plt.close()


# 5. Sales Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Sales"])
plt.title("Sales Distribution and Outliers")
plt.xlabel("Sales")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "boxplot_sales.png"))
plt.close()


# 6. Profit Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Profit"])
plt.title("Profit Distribution and Outliers")
plt.xlabel("Profit")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "boxplot_profit.png"))
plt.close()


# 7. Quantity Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Quantity"])
plt.title("Quantity Distribution and Outliers")
plt.xlabel("Quantity")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "boxplot_quantity.png"))
plt.close()


# 8. Discount Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["Discount"])
plt.title("Discount Distribution and Outliers")
plt.xlabel("Discount")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "boxplot_discount.png"))
plt.close()


print("\nAll 8 visualizations generated successfully!")
print("Check the visualizations folder.")