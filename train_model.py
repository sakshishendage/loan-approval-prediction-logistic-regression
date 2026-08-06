import pandas as pd
import pickle

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression

# Sample dataset
data = {
    "Age": [18,22,25,30,35,40,45,50,28,33,27,38,41,29,36],
    "Income": [20000,30000,40000,50000,60000,70000,80000,90000,45000,55000,35000,65000,75000,48000,62000],
    "Employment": [
        "Unemployed",
        "Employed",
        "Employed",
        "Self-Employed",
        "Employed",
        "Self-Employed",
        "Employed",
        "Employed",
        "Unemployed",
        "Self-Employed",
        "Unemployed",
        "Employed",
        "Self-Employed",
        "Employed",
        "Employed"
    ],
    "LoanApproved": [0,0,0,1,1,1,1,1,0,1,0,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Age", "Income", "Employment"]]
y = df["LoanApproved"]

numeric_features = ["Age", "Income"]
categorical_features = ["Employment"]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X, y)

with open("loan_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model Saved Successfully!")