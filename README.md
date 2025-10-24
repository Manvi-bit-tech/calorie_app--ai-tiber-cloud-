# CalorEase - Nutrition & Wellness Companion

This repository contains the code for "CalorEase," a multi-part wellness application. It consists of:

1.  **A Django Web App (CalorEase):** A web application for analyzing food nutrition. This is the main application deployed on Vercel.
2.  **A Streamlit ML App:** A machine learning model that predicts calories burned during exercise.

[![Live Demo](https://img.shields.io/badge/Live-Demo%20(Vercel)-blue?style=for-the-badge&logo=vercel)](https://calorie-app-ai-tiber-cloud.vercel.app/)

---

## 1. CalorEase - Django Nutrition App

This is the main web application that allows users to analyze the nutritional profile of different foods. It is built with Django and uses the [API-Ninjas Nutrition API](https://api-ninjas.com/api/nutrition) to fetch data.

### Technologies Used

* **Backend:** Django
* **Frontend:** HTML, CSS, JavaScript
* **API:** [API-Ninjas Nutrition API](https://api-ninjas.com/api/nutrition)
* **Deployment:** Vercel

### Local Setup (Django App)

To run the Django application locally:

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/Manvi-bit-tech/calorie_app--ai-tiber-cloud-.git](https://github.com/Manvi-bit-tech/calorie_app--ai-tiber-cloud-.git)
    cd calorie_app--ai-tiber-cloud-
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Run migrations:**
    ```sh
    python manage.py migrate
    ```

4.  **Start the server:**
    ```sh
    python manage.py runserver
    ```
    The application will be running at `http://127.0.0.1:8000/`.

---

## 2. Calorie Burn Prediction Model (Streamlit)

This repository also includes a machine learning model to predict the calories a person burns during exercise. The prediction is based on user inputs like age, gender, weight, heart rate, and exercise duration.

The model is built with `XGBoost` and is designed to be deployed as a standalone [Streamlit](https://streamlit.io/) app.

### Technologies Used

* **Model:** XGBoost (`XGBRegressor`)
* **Data Science:** Python, Pandas, Scikit-learn
* **App Framework:** Streamlit

### How to Run (Streamlit App)

1.  **Ensure you have the required libraries:**
    If you haven't already, install Streamlit:
    ```sh
    pip install streamlit
    ```

2.  **Run the Streamlit app:**
    The file `Streamlit Deployment.py` contains the code for the app.
    ```sh
    streamlit run "Streamlit Deployment.py"
    ```
    This will open a new tab in your browser with the running Streamlit application.

### Machine Learning Model Details

* **Dataset:** The model was trained on a dataset from Kaggle.
    * **Link:** [Kaggle Exercise Dataset](https://www.kaggle.com/datasets/fmendes/fmendesdat263xdemos/data)
* **Training Notebook:** The full process of data cleaning, feature engineering, and model training can be found in the Jupyter Notebook.
    * **Link:** [calorie_prediction_model.ipynb](https://github.com/Manvi-bit-tech/calorie_app--ai-tiber-cloud-/blob/main/calorie_prediction_model.ipynb)
    * **Colab:** [View in Google Colab](https://colab.research.google.com/drive/1jGfin_NBlQiKOnlEZPptPmkB8yKX5XlT?usp=sharing)
