import streamlit as st
import joblib #для загрузки готовой модели


st.write("Это приложение использует натренированную модель с использованием RandomForestClassifier и датасета Disease Prediction Using Machine Learning \nhttps://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning/data \nЗагрузка натренированной RandomForest (Случайный Лес)...")
with st.spinner("Загрузка..."):
    loaded_model = joblib.load('model_random_f.joblib')

st.success("Загрузка модели успешна!")

