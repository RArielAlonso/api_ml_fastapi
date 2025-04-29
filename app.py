# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Inicializar la app
app = FastAPI()

# Cargar modelo
model = joblib.load('model.pkl')

# Definir input esperado
class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Endpoint raíz
@app.get("/")
def read_root():
    return {"message": "API de predicción de Iris con Random Forest"}

# Endpoint de predicción
@app.post("/predict")
def predict(data: IrisData):
    try:
        features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
        prediction = model.predict(features)
        return {"prediction": int(prediction[0])}  # casteamos a int para que sea JSON serializable
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

