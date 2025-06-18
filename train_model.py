import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Sample training data
data = {
    'Day': list(range(1, 11)),
    'Price': [100, 102, 101, 105, 107, 106, 108, 110, 111, 115]
}
df = pd.DataFrame(data)

# Train model
model = LinearRegression()
model.fit(df[['Day']], df['Price'])

# Save model
joblib.dump(model, 'model.pkl')

print("✅ Model trained and saved as model.pkl")
