# Home Price Prediction Backend 🏠💸

This project provides a **FastAPI** backend service for predicting home prices based on input features such as square footage, number of bedrooms, bathrooms, and location in Bangalore. The service uses a **machine learning model** built with **scikit-learn** to estimate the price of a house.

The backend is deployed on **Render**.

You can try the **home price predictor** on the simple web app deployed at:

[**Predict Real Estate Prices**](https://predict-real-estate.onrender.com/) 🌍

**Note**: Since the backend is hosted on a free tier of Render, it may take a few moments for the locations to load initially. Please be patient while the server warms up.

---

## 🌟 Features

1. **Location Names API** 
   - **Endpoint**: `/get_location_names`
   - **Method**: `GET`
   - **Description**: Returns a list of location names used in the model for prediction.

2. **Price Prediction API** 
   - **Endpoint**: `/predict_home_price`
   - **Method**: `POST`
   - **Description**: Accepts input parameters (location, square footage, number of bedrooms, and bathrooms) and returns the estimated price.

---

## 🚀 How to Run the Backend Locally

### 1. Install Dependencies

Ensure you have **Python 3.7+** installed, then install the required packages using `pip`:

```bash
pip install fastapi uvicorn scikit-learn numpy pandas pydantic
```

### 2. Start FastAPI Server

Run the FastAPI server with `uvicorn`:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`, where you can access the APIs.

---

## 🧰 Model Development

The model for predicting home prices was developed using **Jupyter Notebook**, where the following steps were performed:

- **Data Cleaning**: The dataset was cleaned, handling missing values, outliers, and ensuring all features were ready for training.
- **Feature Engineering**: Relevant features were extracted and transformed to improve the model's prediction accuracy.
- **GridSearch**: A grid search was used to find the best model hyperparameters, ensuring optimal performance.
- **Model Scoring**: The model was evaluated using various metrics, such as RMSE, to assess its performance.
- **Prediction Trials**: Multiple prediction attempts were made to ensure the model's stability and accuracy.

Once the model was trained, it was exported using **pickle** to preserve the trained model, and the columns of the dataset were exported as a **JSON file** for future use.

---

## 🔌 FastAPI Integration

The trained model was integrated into the FastAPI backend:

- The **pickle** file containing the trained model was loaded into the FastAPI backend for making predictions.
- The **columns JSON** was loaded as well, allowing the backend to understand and map incoming features to the correct columns.
- The backend API endpoints are now capable of handling incoming requests and making predictions using the trained model.

With this setup, the backend can accept user inputs (location, square footage, number of bedrooms, bathrooms) and return the predicted home price.

---

## 🛠️ Code Structure

- `main.py`: Contains the FastAPI application and API endpoints for prediction.
- `model.pkl`: The serialized machine learning model used for prediction.
- `columns.json`: The JSON file containing the columns used in the model.
- `util.py`: Utility functions used in the backend (e.g., for loading the model and columns).

---

## 🔒 Deployment

The FastAPI backend is deployed on **Render**, a cloud platform for hosting web services. The deployment process is straightforward and involves pushing the backend to the Render platform, where it is automatically deployed and exposed as a REST API.

---

## 🎓 Course Context

This project is part of a **Machine Learning course** offered by **CodeBasics**. The course provides comprehensive knowledge on the fundamentals of machine learning, with hands-on experience in building real-world applications. This project helped solidify core concepts such as model development, data preprocessing, and deployment, offering practical insights into the entire machine learning pipeline.

---

## 🎯 Conclusion

This backend service allows users to predict home prices based on various input features, providing a simple and effective solution for real estate price estimation. The integration of machine learning with FastAPI makes the model accessible via a web interface or API calls. The project is deployed on Render, making it easy to access and scale.
