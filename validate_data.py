import pandas as pd

df = pd.read_csv("youtube_master_dataset.csv")

print("===== DATA VALIDATION REPORT =====")

print("\nTotal Rows:")
print(len(df))

print("\nTotal Columns:")
print(len(df.columns))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())