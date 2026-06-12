import pandas as pd

df = pd.read_csv("youtube_master_dataset.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.fillna("Unknown")

# Save cleaned data
df.to_csv("youtube_cleaned_data.csv", index=False)

print("Data cleaning completed.")
print("Cleaned dataset saved as youtube_cleaned_data.csv")