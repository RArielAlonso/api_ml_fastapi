# train_model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Cargar un dataset ejemplo
iris = load_iris()
X, y = iris.data, iris.target

# Dividir en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un modelo Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Guardar el modelo entrenado
joblib.dump(model, 'model.pkl')

print("Modelo entrenado y guardado como 'model.pkl'")
