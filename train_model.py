import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
df = pd.read_csv("phishing_site_urls.csv")
df['label'] = df['label'].map({'phishing': 0, 'legitimate': 1})

# Features and labels
X = df['url']
y = df['label']

# Convert URL to features
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = RandomForestClassifier()
model.fit(X_vec, y)

# Save model & vectorizer
joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model trained and saved!")
