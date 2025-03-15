import pandas as pd

# Load dataset
df = pd.read_csv("Dataset.csv")

# Convert time columns to datetime format
df['Login Time'] = pd.to_datetime(df['Login Time'])
df['Logout Time'] = pd.to_datetime(df['Logout Time'])

# Calculate active hours
df['Active Duration'] = (df['Logout Time'] - df['Login Time']).dt.total_seconds() / 3600

# View sample data
print(df.head())
