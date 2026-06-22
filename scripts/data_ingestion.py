import os
import pandas as pd

print("=" * 60)
print("Mutual Fund Data Ingestion Started")
print("=" * 60)

data_folder = "data/raw"

# Folder ke andar jitni CSV files hain unki list
files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

print(f"\nTotal CSV Files Found: {len(files)}")

# Ek-ek file ko read karna
for file in files:

    print("\n" + "=" * 60)
    print(f"Reading File: {file}")
    print("=" * 60)

    file_path = os.path.join(data_folder, file)

    # CSV read karo
    df = pd.read_csv(file_path)

    # Shape
    print("\nShape:")
    print(df.shape)

    # Data Types
    print("\nData Types:")
    print(df.dtypes)

    # First 5 Rows
    print("\nFirst 5 Rows:")
    print(df.head())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())