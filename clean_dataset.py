import pandas as pd

# Load original dataset
df = pd.read_csv("data/sms_spam.csv")

# Display original record count
print("Original records:", len(df))

# Remove duplicate records
df_clean = df.drop_duplicates(
    subset=['label', 'message']
).reset_index(drop=True)

# Display cleaning results
print("\nCLEANING RESULTS")
print("Original records:", len(df))
print("Duplicate records removed:", len(df) - len(df_clean))
print("Remaining records:", len(df_clean))

# Check missing values
print("\nMISSING VALUES:")
print(df_clean.isnull().sum())

# Check remaining duplicates
print("\nREMAINING DUPLICATES:")
print(df_clean.duplicated().sum())

# Display class distribution
print("\nCLASS DISTRIBUTION:")
print(df_clean['label'].value_counts())

# Save cleaned dataset
df_clean.to_csv(
    "data/sms_spam_clean.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")