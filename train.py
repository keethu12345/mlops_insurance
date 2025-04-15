import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv("insurance.csv")

# Features and target
X = df.drop("charges", axis=1)
y = df["charges"]

# Categorical and numerical columns
categorical_cols = ["sex", "smoker", "region"]
numerical_cols = ["age", "bmi", "children"]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(drop="first"), categorical_cols)
    ],
    remainder="passthrough"  # keep numerical columns
)

# Model pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model.fit(X_train, y_train)

# Predict & Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"✅ Model trained. MSE: {mse:.2f}")

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
print("✅ Model saved to model.pkl")
