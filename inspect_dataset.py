import pandas as pd

# Load the dataset
df = pd.read_csv("data/sms_spam.csv")

# Display first five records
print("FIRST FIVE RECORDS:")
print(df.head())

# Dataset information
print("\nDATASET INFORMATION:")
df.info()

# Dataset dimensions
print("\nDATASET SHAPE:")
print(df.shape)

# Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Check duplicate records
print("\nDUPLICATE RECORDS:")
print(df.duplicated().sum())

# Class distribution
print("\nCLASS DISTRIBUTION:")
print(df['label'].value_counts())