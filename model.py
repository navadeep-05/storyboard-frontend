import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
import joblib

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("dataset1_cost_yield.csv")

# Target variable
target = "Yield (Quintal/ Hectare)"

# Features
X = df.drop(columns=[target])
y = df[target]

# Separate numerical + categorical features
num_features = X.select_dtypes(include=[np.number]).columns.tolist()
cat_features = X.select_dtypes(include=['object']).columns.tolist()

# -------------------------------
# PREPROCESSING
# -------------------------------
preprocessor = ColumnTransformer(
    transformers=[
        ("num", "passthrough", num_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features)
    ]
)

# -------------------------------
# MODEL PIPELINE
# -------------------------------
model = Pipeline(steps=[
    ("preprocess", preprocessor),
    ("rf", RandomForestRegressor(n_estimators=300, random_state=42))
])

# -------------------------------
# TRAIN / TEST SPLIT
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# TRAIN MODEL
# -------------------------------
model.fit(X_train, y_train)

# -------------------------------
# EVALUATION
# -------------------------------
pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, pred))
r2 = r2_score(y_test, pred)

print("Model Performance:")
print("RMSE:", rmse)
print("R² Score:", r2)

# -------------------------------
# SAVE MODEL
# -------------------------------
joblib.dump(model, "crop_yield_prediction_model.pkl")
print("Model saved as crop_yield_prediction_model.pkl")
