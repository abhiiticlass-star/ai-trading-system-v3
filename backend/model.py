import xgboost as xgb
import joblib

def train_model(X, y):

    model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1
    )

    model.fit(X, y)

    joblib.dump(model, "model.pkl")
