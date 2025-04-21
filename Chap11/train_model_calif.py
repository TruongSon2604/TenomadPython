from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import joblib
import numpy as np

data = fetch_california_housing()
X = data.data
y = data.target 

X = np.delete(X, 5, axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)
scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

joblib.dump(model, 'california_housing_model_no_population.pkl')
joblib.dump(scaler, 'scaler_no_population.pkl')

y_pred = model.predict(X_test_scaled)

