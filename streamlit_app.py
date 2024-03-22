import streamlit as st
import joblib #для загрузки готовой модели


st.write("Это приложение использует натренированную модель с использованием RandomForestClassifier и датасета Disease Prediction Using Machine Learning \nhttps://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning/data")
st.write("Загрузка натренированной RandomForest (Случайный Лес)...")
with st.spinner("Загрузка..."):
    loaded_model = joblib.load('model_random_f.joblib')

st.success("Загрузка модели успешна!")

# Get user inputs
features = ["itching","skin_rash","nodal_skin_eruptions","continuous_sneezing",
            "shivering","chills","joint_pain","stomach_pain","acidity","ulcers_on_tongue",
            "muscle_wasting","vomiting","burning_micturition","spotting_ urination",
            "fatigue","weight_gain","anxiety","cold_hands_and_feets","mood_swings",
            "weight_loss","restlessness","lethargy","patches_in_throat","irregular_sugar_level",
            "cough","high_fever","sunken_eyes","breathlessness","sweating","dehydration",
            "indigestion","headache","yellowish_skin","dark_urine","nausea","loss_of_appetite",
            "pain_behind_the_eyes","back_pain","constipation","abdominal_pain","diarrhoea",
            "mild_fever","yellow_urine","yellowing_of_eyes","acute_liver_failure",
            "fluid_overload","swelling_of_stomach","swelled_lymph_nodes","malaise",
            "blurred_and_distorted_vision","phlegm","throat_irritation","redness_of_eyes",
            "sinus_pressure","runny_nose","congestion","chest_pain","weakness_in_limbs",
            "fast_heart_rate","pain_during_bowel_movements","pain_in_anal_region","bloody_stool",
            "irritation_in_anus","neck_pain","dizziness","cramps","bruising","obesity",
            "swollen_legs","swollen_blood_vessels","puffy_face_and_eyes","enlarged_thyroid",
            "brittle_nails","swollen_extremeties","excessive_hunger","extra_marital_contacts",
            "drying_and_tingling_lips","slurred_speech","knee_pain","hip_joint_pain",
            "muscle_weakness","stiff_neck","swelling_joints","movement_stiffness",
            "spinning_movements","loss_of_balance","unsteadiness","weakness_of_one_body_side",
            "loss_of_smell","bladder_discomfort","foul_smell_of urine","continuous_feel_of_urine",
            "passage_of_gases","internal_itching","toxic_look_(typhos)","depression","irritability",
            "muscle_pain","altered_sensorium","red_spots_over_body","belly_pain","abnormal_menstruation",
            "dischromic _patches","watering_from_eyes","increased_appetite","polyuria","family_history",
            "mucoid_sputum","rusty_sputum","lack_of_concentration","visual_disturbances",
            "receiving_blood_transfusion","receiving_unsterile_injections","coma","stomach_bleeding",
            "distention_of_abdomen","history_of_alcohol_consumption","fluid_overload","blood_in_sputum",
            "prominent_veins_on_calf","palpitations","painful_walking","pus_filled_pimples","blackheads",
            "scurring","skin_peeling","silver_like_dusting","small_dents_in_nails","inflammatory_nails,blister",
            "red_sore_around_nose","yellow_crust_ooze","prognosis"]

#using checkboxes
symptoms = {
    "itching": st.checkbox("Зуд"),
    "skin_rash": st.checkbox("Кожная сыпь"),
    "nodal_skin_eruptions": st.checkbox("тестовая опция"),
    "loss_of_balance": st.checkbox("Потеря равновесия"),
}

#сохранение выбранных симптомов
selected_symptoms = []
for symptom, checkbox in symptoms.items():
    if checkbox:
        selected_symptoms.append(symptom)

#прогнозируем при нажатии кнопки
if st.button("Прогноз"):
    # Assuming model expects numerical features, convert selected symptoms to a list of 1s and 0s
    # based on presence/absence in the selected_symptoms list
    features = [1 if symptom in selected_symptoms else 0 for symptom in symptoms.keys()]
    prediction = loaded_model.predict([features])
    st.write("Прогноз:", prediction[0])
