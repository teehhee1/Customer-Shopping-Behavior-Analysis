import pandas as pd

# Load dataset
df = pd.read_csv("customer_shopping_behavior.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Statistical summary
print("\nSummary Statistics:")
print(df.describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Review Rating values
df["Review Rating"] = df["Review Rating"].fillna(df["Review Rating"].mean())

# Verify missing values are removed
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("cleaned_customer_data.csv", index=False)

print("\nCleaned dataset saved successfully.")