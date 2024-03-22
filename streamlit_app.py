import streamlit as st
import joblib #для загрузки готовой модели


st.write("Это приложение использует натренированную модель с использованием RandomForestClassifier и датасета Disease Prediction Using Machine Learning \nhttps://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning/data")
st.write("Загрузка натренированной RandomForest (Случайный Лес)...")
with st.spinner("Загрузка..."):
    loaded_model = joblib.load('model_random_f.joblib')

st.success("Загрузка модели успешна!")

# Get user inputs
'''
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
'''

#using checkboxes
symptoms = {
    "itching": st.checkbox("Зуд"), # Itching
    "skin_rash": st.checkbox("Кожная сыпь"), # Skin Rash
    "nodal_skin_eruptions": st.checkbox("Узловые кожные высыпания"), # Nodal Skin Eruptions
    "continuous_sneezing": st.checkbox("Продолжительное чихание"), # Continuous Sneezing
    "shivering": st.checkbox("Озноб"),  # Shivering
    "chills": st.checkbox("Тряска"),  # Chills
    "joint_pain": st.checkbox("Боль в суставах"),  # Joint pain
    "stomach_pain": st.checkbox("Боль в животе"),  # Stomach pain
    "acidity": st.checkbox("Изжога"),  # Acidity
    "ulcers_on_tongue": st.checkbox("Язвы на языке"),  # Ulcers on tongue
    "muscle_wasting": st.checkbox("Мышечная атрофия"),  # Muscle wasting
    "vomiting": st.checkbox("Рвота"),  # Vomiting
    "burning_micturition": st.checkbox("Жжение при мочеиспускании"),  # Burning micturition
    "spotting_urination": st.checkbox("Маточное кровотечение"),  # Spotting urination (translated to uterine bleeding)
    "fatigue": st.checkbox("Усталость"),  # Fatigue
    "weight_gain": st.checkbox("Увеличение веса"),  # Weight gain
    "anxiety": st.checkbox("Тревога"),  # Anxiety
    "cold_hands_and_feets": st.checkbox("Холодные руки и ноги"),  # Cold hands and feet
    "mood_swings": st.checkbox("Перепады настроения"),  # Mood swings
    "weight_loss": st.checkbox("Потеря веса"),  # Weight loss
    "restlessness": st.checkbox("Беспокойство"),  # Restlessness
    "lethargy": st.checkbox("Летаргия"),  # Lethargy
    "patches_in_throat": st.checkbox("Пятна в горле"),  # Patches in throat
    "irregular_sugar_level": st.checkbox("Неправильный уровень сахара"),  # Irregular sugar level
    "cough": st.checkbox("Кашель"),  # Cough
    "high_fever": st.checkbox("Высокая температура"),  # High fever
    "sunken_eyes": st.checkbox("Запавшие глаза"),  # Sunken eyes
    "breathlessness": st.checkbox("Одышка"),  # Breathlessness
    "sweating": st.checkbox("Потоотливость"),  # Sweating
    "dehydration": st.checkbox("Обезвоживание"),  # Dehydration
    "indigestion": st.checkbox("Расстройство желудка"),  # Indigestion
    "headache": st.checkbox("Головная боль"),  # Headache
    "yellowish_skin": st.checkbox("Желтушность кожи"),  # Yellowish skin
    "dark_urine": st.checkbox("Темная моча"),  # Dark urine
    "nausea": st.checkbox("Тошнота"),  # Nausea
    "loss_of_appetite": st.checkbox("Потеря аппетита"),  # Loss of appetite
    "pain_behind_the_eyes": st.checkbox("Боль за глазами"),  # Pain behind the eyes
    "back_pain": st.checkbox("Боль в спине"),  # Back pain
    "constipation": st.checkbox("Запор"),  # Constipation
    "abdominal_pain": st.checkbox("Боль в животе"),  # Abdominal pain
    "diarrhoea": st.checkbox("Диарея"),  # Diarrhoea
    "mild_fever": st.checkbox("Небольшой жар"),  # Mild fever
    "yellow_urine": st.checkbox("Желтая моча"),  # Yellow urine (already included)
    "yellowing_of_eyes": st.checkbox("Пожелтение глаз"),  # Yellowing of eyes
    "acute_liver_failure": st.checkbox("Острая печеночная недостаточность"),  # Acute liver failure
    "fluid_overload": st.checkbox("Перегрузка жидкостью"),  # Fluid overload
    "swelling_of_stomach": st.checkbox("Опухоль живота"),  # Swelling of stomach
    "swelled_lymph_nodes": st.checkbox("Увеличенные лимфатические узлы"),  # Swollen lymph nodes
    "malaise": st.checkbox("Недомогание"),  # Malaise
    "blurred_and_distorted_vision": st.checkbox("Затуманенное и искаженное зрение"),  # Blurred and distorted vision
    "phlegm": st.checkbox("Мокрота"),  # Phlegm
    "throat_irritation": st.checkbox("Раздражение горла"),  # Throat irritation
    "redness_of_eyes": st.checkbox("Покраснение глаз"),  # Redness of eyes
    "sinus_pressure": st.checkbox("Заложенность носовых пазух"),  # Sinus pressure
    "runny_nose": st.checkbox("Насморк"),  # Runny nose
    "congestion": st.checkbox("Заложенность носа"),  # Congestion
    "chest_pain": st.checkbox("Боль в груди"),  # Chest pain
    "weakness_in_limbs": st.checkbox("Слабость в конечностях"),  # Weakness in limbs
    "fast_heart_rate": st.checkbox("Учащенное сердцебиение"),  # Fast heart rate
    "pain_during_bowel_movements": st.checkbox("Боль во время дефекации"),  # Pain during bowel movements
    "pain_in_anal_region": st.checkbox("Боль в анальной области"),  # Pain in anal region
    "bloody_stool": st.checkbox("Кровавый стул"),  # Bloody stool
    "irritation_in_anus": st.checkbox("Раздражение в заднем проходе"),  # Irritation in anus
    "neck_pain": st.checkbox("Боль в шее"),  # Neck pain
    "dizziness": st.checkbox("Головокружение"),  # Dizziness
    "cramps": st.checkbox("Судороги"),  # Cramps
    "bruising": st.checkbox("Синяки"),  # Bruising
    "obesity": st.checkbox("Ожирение"),  # Obesity
    "swollen_legs": st.checkbox("Отек ног"),  # Swollen legs
    "swollen_blood_vessels": st.checkbox("Отекшие кровеносные сосуды"),  # Swollen blood vessels
    "puffy_face_and_eyes": st.checkbox("Опухшее лицо и глаза"),  # Puffy face and eyes
    "enlarged_thyroid": st.checkbox("Увеличенная щитовидная железа"),  # Enlarged thyroid
    "brittle_nails": st.checkbox("Ломкие ногти"),  # Brittle nails
    "swollen_extremeties": st.checkbox("Отек конечностей"),  # Swollen extremities
    "excessive_hunger": st.checkbox("Чрезмерный голод"),  # Excessive hunger
    "extra_marital_contacts": st.checkbox("Внебрачные контакты"),  # Extra-marital contacts
    "drying_and_tingling_lips": st.checkbox("Сухие и покалывающие губы"),  # Drying and tingling lips
    "slurred_speech": st.checkbox("Невнятная речь"),  # Slurred speech
    "knee_pain": st.checkbox("Боль в колене"),  # Knee pain
    "hip_joint_pain": st.checkbox("Боль в тазобедренном суставе"),  # Hip joint pain
    "muscle_weakness": st.checkbox("Мышечная слабость"),  # Muscle weakness (already included)
    "stiff_neck": st.checkbox("Жесткая шея"),  # Stiff neck
    "swelling_joints": st.checkbox("Опухшие суставы"),  # Swelling joints
    "movement_stiffness": st.checkbox("Скованность движений"), # Movement Stiffness
    "spinning_movements": st.checkbox("Вращательные движения"),  # Spinning movements
    "loss_of_balance": st.checkbox("Потеря равновесия"),  # Loss of balance
    "unsteadiness": st.checkbox("Неустойчивость"),  # Unsteadiness
    "weakness_of_one_body_side": st.checkbox("Слабость с одной стороны тела"),  # Weakness of one body side
    "loss_of_smell": st.checkbox("Потеря обоняния"),  # Loss of smell
    "bladder_discomfort": st.checkbox("Дискомфорт мочевого пузыря"),  # Bladder discomfort
    "foul_smell_of_urine": st.checkbox("Гнилостный запах мочи"),  # Foul smell of urine
    "continuous_feel_of_urine": st.checkbox("Постоянное чувство мочеиспускания"),  # Continuous feel of urine
    "passage_of_gases": st.checkbox("Отхождение газов"),  # Passage of gases
    "internal_itching": st.checkbox("Внутренний зуд"),  # Internal itching
    "toxic_look_(typhos)": st.checkbox("Токсический взгляд (тиф)"),  # Toxic look (typhoid)
    "depression": st.checkbox("Депрессия"),  # Depression (already included)
    "irritability": st.checkbox("Раздражительность"),  # Irritability (already included)
    "muscle_pain": st.checkbox("Мышечная боль"),  # Muscle pain (already included)
    "altered_sensorium": st.checkbox("Нарушение сознания"),  # Altered sensorium
    "red_spots_over_body": st.checkbox("Красные пятна по всему телу"),  # Red spots over body
    "belly_pain": st.checkbox("Боль в животе"),  # Belly pain (already included)
    "abnormal_menstruation": st.checkbox("Неправильные месячные"),  # Abnormal menstruation
    "dischromic_patches": st.checkbox("Пигментные пятна"),  # Dischromic patches
    "watering_from_eyes": st.checkbox("Слезотечение"),  # Watering from eyes
    "increased_appetite": st.checkbox("Повышенный аппетит"),  # Increased appetite
    "polyuria": st.checkbox("Частое мочеиспускание"),  # Polyuria
    "family_history": st.checkbox("Семейный анамнез"),  # Family history
    "mucoid_sputum": st.checkbox("Мокрота слизистая"),  # Mucoid sputum
    "rusty_sputum": st.checkbox("Ржавая мокрота"),  # Rusty sputum
    "lack_of_concentration": st.checkbox("Рассеянность"),  # Lack of concentration
    "visual_disturbances": st.checkbox("Нарушения зрения"),  # Visual disturbances
    "receiving_blood_transfusion": st.checkbox("Переливание крови"),  # Receiving blood transfusion
    "receiving_unsterile_injections": st.checkbox("Нестерильные инъекции"),  # Receiving unsterile injections
    "coma": st.checkbox("Кома"),  # Coma (already included)
    "stomach_bleeding": st.checkbox("Желудочное кровотечение"),  # Stomach bleeding (already included)
    "distention_of_abdomen": st.checkbox("Вздутие живота"),  # Distention of abdomen
    "history_of_alcohol_consumption": st.checkbox("История употребления алкоголя"),  # History of alcohol consumption
    "fluid_overload": st.checkbox("Перегрузка жидкостью"),  # Fluid overload (already included)
    "blood_in_sputum": st.checkbox("Кровь в мокроте"),  # Blood in sputum
    "prominent_veins_on_calf": st.checkbox("Выступающие вены на голени"),  # Prominent veins on calf
    "palpitations": st.checkbox("Сердцебиение"),  # Palpitations
    "painful_walking": st.checkbox("Болезненная ходьба"),  # Painful walking
    "pus_filled_pimples": st.checkbox("Гнойные прыщи"),  # Pus-filled pimples
    "blackheads": st.checkbox("Черные точки"),  # Blackheads
    "scurring": st.checkbox("Рубцевание"),  # Scarring
    "skin_peeling": st.checkbox("Шелушение кожи"),  # Skin peeling
    "silver_like_dusting": st.checkbox("Серебряный налет"),  # Silver-like dusting
    "small_dents_in_nails": st.checkbox("Вмятины на ногтях"),  # Small dents in nails
    "inflammatory_nails,blister": st.checkbox("Воспаление ногтей, волдыри"),  # Inflammatory nails, blister (combined)
    "red_sore_around_nose": st.checkbox("Красная язва вокруг носа"),  # Red sore around nose
    "yellow_crust_ooze": st.checkbox("Желтый экссудат"),  # Yellow crust ooze
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
    st.write(f"{features}, \n{selected_symptoms}\n\n")
    prediction = loaded_model.predict([features])
    st.write("Прогноз:", prediction[0])
