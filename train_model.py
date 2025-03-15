from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load processed dataset
df = pd.read_csv("processed_dataset.csv")

# Target variable: 1 if doctor attended survey, 0 otherwise
df['Attended Survey'] = (df['Count of Survey Attempts'] > 1).astype(int)

# Select features
features = ['Active Duration']
X = df[features]
y = df['Attended Survey']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
import joblib
joblib.dump(model, "survey_model.pkl")

print("Model trained and saved.")

