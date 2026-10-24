
import pandas as pd
from pathlib import Path

# ==================================================
# TASK 3: DATASET SELECTION & DATA PREPARATION
# Domain: Sales and Retail Analytics
# Dataset: Sample Superstore
# ==================================================

# 1. Define project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "Sample - Superstore.xlsx"
OUTPUT_FILE = PROJECT_DIR / "data" / "Sample - Superstore-Cleaned.xlsx"

# 2. Load dataset
print("=" * 65)
print("TASK 3: DATASET SELECTION & DATA PREPARATION")
print("=" * 65)

df = pd.read_excel(
    DATA_FILE,
    sheet_name="Sample - Superstore"
)

# Preserve the original data for comparison
original_df = df.copy()

# 3. Dataset selection
print("\n1. DATASET SELECTION")
print("Domain: Sales and Retail Analytics")
print("Dataset: Sample Superstore")
print("Purpose: Analyze sales, profit, customers, and products.")

# 4. Data inspection
print("\n2. DATA INSPECTION")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\nFirst five records:")
print(df.head().to_string(index=False))

# 5. Identify columns and data types
print("\n3. COLUMN NAMES AND DATA TYPES")
print(df.dtypes.to_string())

print("\nDetailed dataset information:")
df.info()

# 6. Identify missing values
print("\n4. MISSING VALUES BEFORE CLEANING")
missing_before = df.isnull().sum()
print(missing_before.to_string())

print("\nTotal missing values:", int(missing_before.sum()))

# 7. Standardize column names and text values
df.columns = df.columns.str.strip()

text_columns = df.select_dtypes(
    include=["object", "string"]
).columns

for column in text_columns:
    df[column] = df[column].apply(
        lambda value: value.strip()
        if isinstance(value, str)
        else value
    )

# 8. Handle missing values
print("\n5. HANDLING MISSING VALUES")

for column in df.columns:

    missing_count = df[column].isnull().sum()

    if missing_count == 0:
        continue

    # Fill missing numeric values with the median
    if pd.api.types.is_numeric_dtype(df[column]):
        df[column] = df[column].fillna(
            df[column].median()
        )

    # Fill missing text values with the mode
    elif (
        pd.api.types.is_object_dtype(df[column])
        or pd.api.types.is_string_dtype(df[column])
    ):
        mode_values = df[column].mode(dropna=True)

        if not mode_values.empty:
            df[column] = df[column].fillna(
                mode_values.iloc[0]
            )

print("Missing values handled where a suitable")
print("replacement value was available.")

# 9. Convert date columns
print("\n6. DATE VALIDATION")

for column in ["Order Date", "Ship Date"]:

    if column in df.columns:
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )

        print(
            f"{column}:",
            df[column].isna().sum(),
            "missing or invalid date values"
        )

# 10. Check duplicates
print("\n7. DUPLICATE RECORDS")

duplicate_count = int(df.duplicated().sum())

print("Duplicate rows found:", duplicate_count)

df = df.drop_duplicates()

print("Duplicate rows removed:", duplicate_count)

# 11. Validate important numeric columns
print("\n8. NUMERIC DATA VALIDATION")

for column in ["Sales", "Quantity", "Discount", "Profit"]:

    if column in df.columns:
        print(f"\n{column} summary:")
        print(df[column].describe().to_string())

# 12. Check remaining missing values
print("\n9. MISSING VALUES AFTER CLEANING")

missing_after = df.isnull().sum()
print(missing_after.to_string())

print("\nTotal remaining missing values:",
      int(missing_after.sum()))

# 13. Save cleaned dataset
df.to_excel(
    OUTPUT_FILE,
    index=False
)

# 14. Final summary
print("\n10. FINAL CLEANING SUMMARY")
print("Original rows:", len(original_df))
print("Final rows:", len(df))
print("Rows removed:", len(original_df) - len(df))
print("Original columns:", len(original_df.columns))
print("Final columns:", len(df.columns))

print("\nCleaned dataset saved to:")
print(OUTPUT_FILE)

# 11. FINAL DATA VALIDATION

print("\n11. FINAL DATA VALIDATION")

# Check for negative sales and quantities
print("Negative sales records:", (df["Sales"] < 0).sum())
print("Non-positive quantity records:", (df["Quantity"] <= 0).sum())

# Check for invalid discounts
print(
    "Discounts outside the 0-1 range:",
    ((df["Discount"] < 0) | (df["Discount"] > 1)).sum()
)

# Check for missing or invalid dates
print("Invalid order dates:", df["Order Date"].isna().sum())
print("Invalid ship dates:", df["Ship Date"].isna().sum())

# Check shipping dates
print(
    "Ship dates before order dates:",
    (df["Ship Date"] < df["Order Date"]).sum()
)

print("\nFinal dataset shape:", df.shape)
print("DATA VALIDATION COMPLETED")
print("\nTASK 3 COMPLETED SUCCESSFULLY!")