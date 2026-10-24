import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# TASK 4: EXPLORATORY DATA ANALYSIS (EDA)
# Project: Sample Superstore Sales Analysis
# ============================================================

# 1. PROJECT PATHS
PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = PROJECT_DIR / "data" / "Sample - Superstore-Cleaned.xlsx"
OUTPUT_DIR = PROJECT_DIR / "visualizations"
REPORT_DIR = PROJECT_DIR / "report"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# 2. LOAD DATASET
print("=" * 65)
print("TASK 4: EXPLORATORY DATA ANALYSIS")
print("=" * 65)

df = pd.read_excel(DATA_FILE)

# Standardize column names by removing extra spaces
df.columns = df.columns.str.strip()

print("\n1. DATASET INSPECTION")
print("-" * 40)
print("Dataset shape:", df.shape)
print("\nFirst five rows:")
print(df.head().to_string(index=False))

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes.to_string())

print("\nDataset information:")
df.info()

# 3. DATA CLEANING
print("\n2. DATA CLEANING")
print("-" * 40)

original_rows = len(df)

# Remove completely duplicated rows
duplicate_count = int(df.duplicated().sum())
print("Completely duplicated rows:", duplicate_count)

df = df.drop_duplicates().copy()

# Convert date columns into datetime format
for col in ["Order Date", "Ship Date"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# Convert numeric columns into numeric format
numeric_columns = ["Sales", "Profit", "Quantity", "Discount"]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

print("Rows before cleaning:", original_rows)
print("Rows after duplicate removal:", len(df))
print("Rows removed:", original_rows - len(df))

# 4. MISSING-VALUE ANALYSIS
print("\n3. MISSING-VALUE ANALYSIS")
print("-" * 40)

missing_before = df.isnull().sum()

print("\nMissing values before handling:")
print(missing_before.to_string())
print("Total missing values:", int(missing_before.sum()))

# Save missing-value report
missing_report = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values,
    "Missing Percentage": (
        df.isnull().sum().values / len(df) * 100
    ).round(2)
})

missing_report.to_csv(
    REPORT_DIR / "eda_missing_values.csv", index=False
)

# Handle missing numeric values using median
for col in df.select_dtypes(include="number").columns:
    if df[col].isnull().any():
        median_value = df[col].median()

        if pd.notna(median_value):
            df[col] = df[col].fillna(median_value)

# Handle missing categorical values using mode
for col in df.select_dtypes(include=["object", "category"]).columns:
    if df[col].isnull().any():
        mode_values = df[col].mode(dropna=True)

        if not mode_values.empty:
            df[col] = df[col].fillna(mode_values.iloc[0])

# Missing dates cannot be reliably imputed without justification.
# Remove records with invalid/missing critical dates.
date_columns = [
    col for col in ["Order Date", "Ship Date"] if col in df.columns
]

if date_columns:
    df = df.dropna(subset=date_columns).copy()

print("\nMissing values after handling:")
print(df.isnull().sum().to_string())
print("Total remaining missing values:", int(df.isnull().sum().sum()))

# 5. DESCRIPTIVE STATISTICS
print("\n4. DESCRIPTIVE STATISTICS")
print("-" * 40)

numeric_df = df.select_dtypes(include="number")

descriptive_stats = numeric_df.describe().T
descriptive_stats["median"] = numeric_df.median()
descriptive_stats["variance"] = numeric_df.var()

print(descriptive_stats.round(2).to_string())

descriptive_stats.to_csv(
    REPORT_DIR / "eda_descriptive_statistics.csv"
)

# 6. CORRELATION ANALYSIS
print("\n5. CORRELATION ANALYSIS")
print("-" * 40)

correlation_columns = [
    col for col in ["Sales", "Profit", "Quantity", "Discount"]
    if col in df.columns
]

correlation_matrix = df[correlation_columns].corr()

print(correlation_matrix.round(3).to_string())

correlation_matrix.to_csv(
    REPORT_DIR / "eda_correlation_matrix.csv"
)

# Create correlation heatmap using Matplotlib
fig, ax = plt.subplots(figsize=(8, 6))

image = ax.imshow(
    correlation_matrix,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

ax.set_xticks(range(len(correlation_columns)))
ax.set_yticks(range(len(correlation_columns)))

ax.set_xticklabels(correlation_columns, rotation=45, ha="right")
ax.set_yticklabels(correlation_columns)

for i in range(len(correlation_columns)):
    for j in range(len(correlation_columns)):
        ax.text(
            j, i,
            f"{correlation_matrix.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

ax.set_title("Correlation Heatmap - Superstore Dataset")
fig.colorbar(image, ax=ax, label="Correlation")
fig.tight_layout()

fig.savefig(
    OUTPUT_DIR / "correlation_heatmap.png",
    dpi=150,
    bbox_inches="tight"
)
plt.close(fig)

# 7. CATEGORY-WISE AND REGION-WISE ANALYSIS
print("\n6. CATEGORY AND REGION ANALYSIS")
print("-" * 40)

if "Category" in df.columns:
    category_analysis = df.groupby("Category").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum")
    ).sort_values("Total_Sales", ascending=False)

    print("\nCategory-wise performance:")
    print(category_analysis.round(2).to_string())

    category_analysis.to_csv(
        REPORT_DIR / "eda_category_analysis.csv"
    )

    ax = category_analysis["Total_Sales"].plot(
        kind="bar", figsize=(9, 5), title="Sales by Category"
    )
    ax.set_xlabel("Category")
    ax.set_ylabel("Total Sales")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "sales_by_category.png",
        dpi=150,
        bbox_inches="tight"
    )
    plt.close()

if "Region" in df.columns:
    region_analysis = df.groupby("Region").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    ).sort_values("Total_Sales", ascending=False)

    print("\nRegion-wise performance:")
    print(region_analysis.round(2).to_string())

    region_analysis.to_csv(
        REPORT_DIR / "eda_region_analysis.csv"
    )

    ax = region_analysis["Total_Sales"].plot(
        kind="bar", figsize=(9, 5), title="Sales by Region"
    )
    ax.set_xlabel("Region")
    ax.set_ylabel("Total Sales")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "sales_by_region.png",
        dpi=150,
        bbox_inches="tight"
    )
    plt.close()

# 8. SALES TREND OVER TIME
print("\n7. SALES TREND ANALYSIS")
print("-" * 40)

if "Order Date" in df.columns and "Sales" in df.columns:
    monthly_sales = (
        df.set_index("Order Date")["Sales"]
        .resample("MS")
        .sum()
    )

    print("\nMonthly sales:")
    print(monthly_sales.round(2).to_string())

    monthly_sales.to_csv(
        REPORT_DIR / "eda_monthly_sales.csv",
        header=["Total Sales"]
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(
        monthly_sales.index,
        monthly_sales.values,
        marker="o"
    )
    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Sales")
    fig.autofmt_xdate()
    fig.tight_layout()

    fig.savefig(
        OUTPUT_DIR / "monthly_sales_trend.png",
        dpi=150,
        bbox_inches="tight"
    )
    plt.close(fig)

# 9. OUTLIER DETECTION USING IQR
print("\n8. OUTLIER DETECTION")
print("-" * 40)

outlier_results = []

for col in ["Sales", "Profit", "Quantity", "Discount"]:
    if col not in df.columns:
        continue

    values = df[col].dropna()

    if values.empty:
        continue

    q1 = values.quantile(0.25)
    q3 = values.quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outlier_mask = (values < lower_bound) | (values > upper_bound)
    outlier_count = int(outlier_mask.sum())

    outlier_results.append({
        "Column": col,
        "Q1": q1,
        "Q3": q3,
        "IQR": iqr,
        "Lower Bound": lower_bound,
        "Upper Bound": upper_bound,
        "Outlier Count": outlier_count,
        "Outlier Percentage": round(
            outlier_count / len(values) * 100, 2
        )
    })

    print(f"\n{col}:")
    print("Lower bound:", round(lower_bound, 2))
    print("Upper bound:", round(upper_bound, 2))
    print("Potential outliers:", outlier_count)

outlier_report = pd.DataFrame(outlier_results)

outlier_report.to_csv(
    REPORT_DIR / "eda_outlier_report.csv", index=False
)

# Generate boxplots
for col in ["Sales", "Profit", "Quantity", "Discount"]:
    if col not in df.columns:
        continue

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.boxplot(df[col].dropna())
    ax.set_title(f"Outlier Detection - {col}")
    ax.set_ylabel(col)
    fig.tight_layout()

    fig.savefig(
        OUTPUT_DIR / f"boxplot_{col.lower()}.png",
        dpi=150,
        bbox_inches="tight"
    )
    plt.close(fig)

# 10. PREPARE AUTOMATIC FINDINGS
print("\n9. KEY FINDINGS")
print("-" * 40)

findings = []

if "Category" in df.columns and "Sales" in df.columns:
    category_sales = df.groupby("Category")["Sales"].sum()
    best_category = category_sales.idxmax()

    finding = (
        f"The category with the highest total sales is "
        f"{best_category} ({category_sales.max():.2f})."
    )
    findings.append(finding)
    print(finding)

if "Region" in df.columns and "Sales" in df.columns:
    region_sales = df.groupby("Region")["Sales"].sum()
    best_region = region_sales.idxmax()

    finding = (
        f"The region with the highest total sales is "
        f"{best_region} ({region_sales.max():.2f})."
    )
    findings.append(finding)
    print(finding)

if "Profit" in df.columns:
    total_profit = df["Profit"].sum()
    finding = f"Total profit across the analysed records is {total_profit:.2f}."
    findings.append(finding)
    print(finding)

if "Sales" in correlation_matrix.columns and "Profit" in correlation_matrix.columns:
    sales_profit_corr = correlation_matrix.loc["Sales", "Profit"]

    finding = (
        f"The Pearson correlation between Sales and Profit is "
        f"{sales_profit_corr:.3f}. Correlation indicates association, "
        f"not causation."
    )
    findings.append(finding)
    print(finding)

if "Discount" in correlation_matrix.columns and "Profit" in correlation_matrix.columns:
    discount_profit_corr = correlation_matrix.loc["Discount", "Profit"]

    finding = (
        f"The Pearson correlation between Discount and Profit is "
        f"{discount_profit_corr:.3f}. Further analysis is needed before "
        f"concluding how discounts affect profitability."
    )
    findings.append(finding)
    print(finding)

findings.append(
    f"Final analysed dataset contains {len(df)} rows and {len(df.columns)} columns."
)

# Save final findings
with open(REPORT_DIR / "eda_findings.txt", "w", encoding="utf-8") as file:
    file.write("TASK 4: EXPLORATORY DATA ANALYSIS FINDINGS\n")
    file.write("=" * 50 + "\n\n")

    for item in findings:
        file.write("- " + item + "\n")

    file.write("\nMissing values after handling:\n")
    file.write(str(int(df.isnull().sum().sum())) + "\n")

    file.write("\nFinal dataset shape:\n")
    file.write(str(df.shape) + "\n")

# Save the final analysis dataset
df.to_excel(
    DATA_FILE.parent / "Sample - Superstore-EDA.xlsx",
    index=False
)

print("\n" + "=" * 65)
print("TASK 4 EDA COMPLETED SUCCESSFULLY!")
print("=" * 65)

print("\nGenerated outputs:")
print("Visualizations folder:", OUTPUT_DIR)
print("Reports folder:", REPORT_DIR)
print("Final EDA dataset: data/Sample - Superstore-EDA.xlsx")
print("\nReview the generated reports and charts before submission.")