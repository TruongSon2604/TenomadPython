from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X = [
    [50, 2, 1],
    [60, 3, 1],
    [80, 3, 2],
    [120, 4, 3],
    [100, 3, 2],
    [50, 2, 1],
    [60, 3, 1],
    [80, 3, 2],
    [120, 4, 3],
    [100, 3, 2],
]
X_scaled = scaler.fit_transform(X)
y = [500, 600, 800, 1200, 1000]
model = LogisticRegression(max_iter=1000)
model.fit(X_scaled, y)
joblib.dump(model, "model.pkl")


