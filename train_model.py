import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv('jantung.csv')
df.columns = df.columns.str.strip().str.lower()

X = df.drop(columns='death_event')
y = df['death_event']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model berhasil dilatih dan disimpan sebagai 'model.pkl'")
