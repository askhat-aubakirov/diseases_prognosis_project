import streamlit as st
import joblib #для загрузки готовой модели


st.write("Загрузка натренированной RandomForest (Случайный Лес)...")
with st.spinner("Загрузка..."):
    loaded_model = joblib.load('model_random_f.joblib')

st.success("Загрузка модели успешна!")

