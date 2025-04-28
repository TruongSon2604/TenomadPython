from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
import joblib
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

X = np.array([[i] for i in range(1, 51)])
np.random.seed(42)
noise = np.random.normal(0, 5, size=X.shape[0])
y = 50 + 3 * X.flatten() + noise
y = np.clip(np.round(y / 2) * 2, 0, 100) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = LinearRegression()

model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mape = mean_absolute_percentage_error(y_test, y_pred) * 100

print(f"MAPE (độ chính xác của mô hình theo %): {mape:.4f}%")
print(f"Điểm dự đoán: {y_pred}")
print(f"Điểm thực tế: {y_test}")
print(f"rmse: {rmse:.10f}")
print(f"mape: {mape:.10f}")

joblib.dump(model, "student_score_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(rmse, "rmse.pkl")
joblib.dump(mape, "mape.pkl")