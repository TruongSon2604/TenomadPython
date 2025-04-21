from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
import joblib


X = np.array([[1, 50], [2, 55], [3, 60], [4, 65], [5, 70], [6, 75], [7, 80], [8, 85], [9, 90], [10, 95]])
y = np.array([55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = LinearRegression()

model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

print(f"Điểm dự đoán: {y_pred}")
print(f"Điểm thực tế: {y_test}")

joblib.dump(model, "student_score_model.pkl")
joblib.dump(scaler, "scaler.pkl")
