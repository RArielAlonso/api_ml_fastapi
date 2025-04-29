# :four_leaf_clover: Iris Machine Learning API (FastAPI + Docker)

This project provides a simple **REST API** for predicting **Iris flower species** using a trained `RandomForestClassifier` from scikit-learn.  
The API is built with **FastAPI** and can be deployed using **Docker**.

---

## :rocket: Features

- Predicts Iris species (`setosa`, `versicolor`, `virginica`)  
- Built with **FastAPI** for high performance  
- **Automatic API documentation** at `/docs`  
- **Containerized** using Docker for easy deployment  
- Simple **JSON-based API** for easy integration  

---

## :hammer: Requirements

Make sure you have installed:

- **Python 3.8+**
- **Docker** (to run the API in a container)

---

##  Setup & Usage

### :one: Clone the repository  
```
git clone https://github.com/your-username/iris-ml-api.git
cd iris-ml-api
```

### :two:Build Docker image
```
docker build -t iris-ml-api .
```

### :three: Run container

```
docker run -d -p 8000:8000 iris-ml-api
```
Visit: http://localhost:8000/docs

### :four: Make a Prediction

#### Endpoint: POST /predict

Example request:


```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```
**Example response:**

```json
{
  "prediction": 0
}

```

**Class Mapping:**

0 = setosa
1 = versicolor
2 = virginica
