import pandas as pd
from pathlib import Path

# Locate the downloaded dataset
file_path = Path("data/SMSSpamCollection")

# Read the original dataset
df = pd.read_csv(
    file_path,
    sep='\t',
    header=None,
    names=['label', 'message'],
    encoding='utf-8'
)

# Display dataset information
print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

print("\nFirst five records:")
print(df.head())

print("\nClass distribution:")
print(df['label'].value_counts())

# Save as CSV
df.to_csv("data/sms_spam.csv", index=False)

print("\nDataset saved successfully as data/sms_spam.csv")