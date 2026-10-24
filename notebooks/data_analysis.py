
import pandas as pd
from pathlib import Path

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "Sample - Superstore.xlsx"

# Load the dataset
df = pd.read_excel(DATA_FILE, sheet_name="Sample - Superstore")

# Display basic information
print("AMAZON? No — SAMPLE SUPERSTORE DATA ANALYSIS")
print("-" * 45)

print("\nFirst five rows:")
print(df.head())

print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types and non-null counts:")
df.info()

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nDescriptive statistics:")
print(df.describe(include="all").T)
