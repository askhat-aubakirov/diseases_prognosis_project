import streamlit as st
import joblib #для загрузки готовой модели


st.write("Это приложение использует натренированную модель с использованием RandomForestClassifier и датасета Disease Prediction Using Machine Learning \nhttps://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning/data")
st.write("Загрузка натренированной RandomForest (Случайный Лес)...")
with st.spinner("Загрузка..."):
    loaded_model = joblib.load('model_random_f.joblib')

st.success("Загрузка модели успешна!")

st.write("Выберите из списка наблюдаемые симптомы:")

# Get user inputs
#using checkboxes
symptoms = {
    "itching": st.checkbox("Зуд", key="itching"), # Itching
    "skin_rash": st.checkbox("Кожная сыпь", key="skin_rash"), # Skin Rash
    "nodal_skin_eruptions": st.checkbox("Узловые кожные высыпания", key="nodal_skin_eruptions"), # Nodal Skin Eruptions
    "continuous_sneezing": st.checkbox("Продолжительное чихание", key="continuous_sneezing"), # Continuous Sneezing
    "shivering": st.checkbox("Озноб", key="shivering"),  # Shivering
    "chills": st.checkbox("Озноб", key="chills"),  # Chills
    "joint_pain": st.checkbox("Боль в суставах", key="joint_pain"),  # Joint pain
    "stomach_pain": st.checkbox("Боль в желудке", key="stomach_pain"),  # Stomach pain
    "acidity": st.checkbox("Изжога (кислотность)", key="acidity"),  # Acidity
    "ulcers_on_tongue": st.checkbox("Язвы на языке", key="ulcers_on_tongue"),  # Ulcers on tongue
    "muscle_wasting": st.checkbox("Мышечная атрофия", key="muscle_wasting"),  # Muscle wasting
    "vomiting": st.checkbox("Рвота", key="vomiting"),  # Vomiting
    "burning_micturition": st.checkbox("Жжение при мочеиспускании", key="burning_micturition"),  # Burning micturition
    "spotting_ urination": st.checkbox("Кровянистые выделения при мочеиспускании", key="spotting_urination"),  # Spotting urination (translated to uterine bleeding)
    "fatigue": st.checkbox("Усталость", key="fatigue"),  # Fatigue
    "weight_gain": st.checkbox("Увеличение веса", key="weight_gain"),  # Weight gain
    "anxiety": st.checkbox("Тревога", key="anxiety"),  # Anxiety
    "cold_hands_and_feets": st.checkbox("Холодные руки и ноги", key="cold_hands_and_feets"),  # Cold hands and feet
    "mood_swings": st.checkbox("Перепады настроения", key="mood_swings"),  # Mood swings
    "weight_loss": st.checkbox("Потеря веса", key="weight_loss"),  # Weight loss
    "restlessness": st.checkbox("Беспокойство", key="restlessness"),  # Restlessness
    "lethargy": st.checkbox("Летаргия", key="lethargy"),  # Lethargy
    "patches_in_throat": st.checkbox("Пятна в горле", key="patches_in_throat"),  # Patches in throat
    "irregular_sugar_level": st.checkbox("Ненормальный и нестабильный уровень сахара", key="irregular_sugar_level"),  # Irregular sugar level
    "cough": st.checkbox("Кашель", key="cough"),  # Cough
    "high_fever": st.checkbox("Высокая температура", key="high_fever"),  # High fever
    "sunken_eyes": st.checkbox("Запавшие глаза", key="sunken_eyes"),  # Sunken eyes
    "breathlessness": st.checkbox("Одышка", key="breathlessness"),  # Breathlessness
    "sweating": st.checkbox("Потливость", key="sweating"),  # Sweating
    "dehydration": st.checkbox("Обезвоживание", key="dehydration"),  # Dehydration
    "indigestion": st.checkbox("Расстройство пищеварения", key="indigestion"),  # Indigestion
    "headache": st.checkbox("Головная боль", key="headache"),  # Headache
    "yellowish_skin": st.checkbox("Желтушность кожи", key="yellowish_skin"),  # Yellowish skin
    "dark_urine": st.checkbox("Темная моча", key="dark_urine"),  # Dark urine
    "nausea": st.checkbox("Тошнота", key="nausea"),  # Nausea
    "loss_of_appetite": st.checkbox("Потеря аппетита", key="loss_of_appetite"),  # Loss of appetite
    "pain_behind_the_eyes": st.checkbox("Боль за глазами", key="pain_behind_the_eyes"),  # Pain behind the eyes
    "back_pain": st.checkbox("Боль в спине", key="back_pain"),  # Back pain
    "constipation": st.checkbox("Запор", key="constipation"),  # Constipation
    "abdominal_pain": st.checkbox("Боль в животе", key="abdominal_pain"),  # Abdominal pain
    "diarrhoea": st.checkbox("Диарея", key="diarrhoea"),  # Diarrhoea
    "mild_fever": st.checkbox("Небольшой жар", key="mild_fever"),  # Mild fever
    "yellow_urine": st.checkbox("Насыщенно желтая моча", key="yellow_urine"),  # Yellow urine (already included)
    "yellowing_of_eyes": st.checkbox("Пожелтение склеры глаза", key="yellowing_of_eyes"),  # Yellowing of eyes
    "acute_liver_failure": st.checkbox("Острая печеночная недостаточность", key="acute_liver_failure"),  # Acute liver failure
    "swelling_of_stomach": st.checkbox("Отечный живот", key="swelling_of_stomach"),  # Swelling of stomach
    "swelled_lymph_nodes": st.checkbox("Увеличенные лимфатические узлы", key="swelled_lymph_nodes"),  # Swollen lymph nodes
    "malaise": st.checkbox("Недомогание", key="malaise"),  # Malaise
    "blurred_and_distorted_vision": st.checkbox("Затуманенное и искаженное зрение", key="blurred_and_distorted_vision"),  # Blurred and distorted vision
    "phlegm": st.checkbox("Выделение мокроты", key="phlegm"),  # Phlegm
    "throat_irritation": st.checkbox("Раздражение горла", key="throat_irritation"),  # Throat irritation
    "redness_of_eyes": st.checkbox("Покраснение глаз", key="redness_of_eyes"),  # Redness of eyes
    "sinus_pressure": st.checkbox("Заложенность носовых пазух", key="sinus_pressure"),  # Sinus pressure
    "runny_nose": st.checkbox("Насморк", key="runny_nose"),  # Runny nose
    "congestion": st.checkbox("Заложенность носа", key="congestion"),  # Congestion
    "chest_pain": st.checkbox("Боль в груди", key="chest_pain"),  # Chest pain
    "weakness_in_limbs": st.checkbox("Слабость в конечностях", key="weakness_in_limbs"),  # Weakness in limbs
    "fast_heart_rate": st.checkbox("Учащенное сердцебиение", key="fast_heart_rate"),  # Fast heart rate
    "pain_during_bowel_movements": st.checkbox("Боль во время дефекации", key="pain_during_bowel_movements"),  # Pain during bowel movements
    "pain_in_anal_region": st.checkbox("Боль в анальной области", key="pain_in_anal_region"),  # Pain in anal region
    "bloody_stool": st.checkbox("Кровавый стул", key="bloody_stool"),  # Bloody stool
    "irritation_in_anus": st.checkbox("Раздражение в заднем проходе", key="irritation_in_anus"),  # Irritation in anus
    "neck_pain": st.checkbox("Боль в шее", key="neck_pain"),  # Neck pain
    "dizziness": st.checkbox("Головокружение", key="dizziness"),  # Dizziness
    "cramps": st.checkbox("Судороги", key="cramps"),  # Cramps
    "bruising": st.checkbox("Синяки", key="bruising"),  # Bruising
    "obesity": st.checkbox("Ожирение", key="obesity"),  # Obesity
    "swollen_legs": st.checkbox("Отек ног", key="swollen_legs"),  # Swollen legs
    "swollen_blood_vessels": st.checkbox("Отекшие кровеносные сосуды", key="swollen_blood_vessels"),  # Swollen blood vessels
    "puffy_face_and_eyes": st.checkbox("Опухшее лицо и глаза", key="puffy_face_and_eyes"),  # Puffy face and eyes
    "enlarged_thyroid": st.checkbox("Увеличенная щитовидная железа", key="enlarged_thyroid"),  # Enlarged thyroid
    "brittle_nails": st.checkbox("Ломкие ногти", key="brittle_nails"),  # Brittle nails
    "swollen_extremeties": st.checkbox("Отек конечностей", key="swollen_extremeties"),  # Swollen extremities
    "excessive_hunger": st.checkbox("Чрезмерный голод", key="excessive_hunger"),  # Excessive hunger
    "extra_marital_contacts": st.checkbox("Внебрачные контакты", key="extra_marital_contacts"),  # Extra-marital contacts
    "drying_and_tingling_lips": st.checkbox("Сухие и трескающиеся губы", key="drying_and_tingling_lips"),  # Drying and tingling lips
    "slurred_speech": st.checkbox("Невнятная речь", key="slurred_speech"),  # Slurred speech
    "knee_pain": st.checkbox("Боль в колене", key="knee_pain"),  # Knee pain
    "hip_joint_pain": st.checkbox("Боль в тазобедренном суставе", key="hip_joint_pain"),  # Hip joint pain
    "muscle_weakness": st.checkbox("Мышечная слабость", key="muscle_weakness"),  # Muscle weakness
    "stiff_neck": st.checkbox("Напряженная шея", key="stiff_neck"),  # Stiff neck
    "swelling_joints": st.checkbox("Опухшие суставы", key="swelling_joints"),  # Swelling joints
    "movement_stiffness": st.checkbox("Скованность движений", key="movement_stiffness"),  # Movement stiffness
    "spinning_movements": st.checkbox("Головокружение", key="spinning_movements"),  # Spinning movements
    "loss_of_balance": st.checkbox("Потеря равновесия", key="loss_of_balance"),  # Loss of balance
    "unsteadiness": st.checkbox("Неустойчивость", key="unsteadiness"),  # Unsteadiness
    "weakness_of_one_body_side": st.checkbox("Слабость с одной стороны тела", key="weakness_of_one_body_side"),  # Weakness of one body side
    "loss_of_smell": st.checkbox("Потеря обоняния", key="loss_of_smell"),  # Loss of smell
    "bladder_discomfort": st.checkbox("Дискомфорт мочевого пузыря", key="bladder_discomfort"),  # Bladder discomfort
    "foul_smell_of urine": st.checkbox("Гнилостный запах мочи", key="foul_smell_of_urine"),  # Foul smell of urine
    "continuous_feel_of_urine": st.checkbox("Постоянное чувство мочеиспускания", key="continuous_feel_of_urine"),  # Continuous feel of urine
    "passage_of_gases": st.checkbox("Отхождение газов", key="passage_of_gases"),  # Passage of gases
    "internal_itching": st.checkbox("Внутренний зуд", key="internal_itching"),  # Internal itching
    "toxic_look_(typhos)": st.checkbox("Тифозный статус", key="toxic_look_(typhos)"),  # Toxic look (typhoid)
    "depression": st.checkbox("Депрессия", key="depression"),  # Depression
    "irritability": st.checkbox("Раздражительность", key="irritability"),  # Irritability
    "muscle_pain": st.checkbox("Мышечная боль", key="muscle_pain"),  # Muscle pain
    "altered_sensorium": st.checkbox("Нарушение сознания", key="altered_sensorium"),  # Altered sensorium
    "red_spots_over_body": st.checkbox("Красные пятна по всему телу", key="red_spots_over_body"),  # Red spots over body
    "belly_pain": st.checkbox("Боль в животе (поверхностная, на уровне большого сальника)", key="belly_pain"),  # Belly pain
    "abnormal_menstruation": st.checkbox("Неправильные месячные", key="abnormal_menstruation"),  # Abnormal menstruation
    "dischromic _patches": st.checkbox("Пигментные пятна", key="dischromic_patches"),  # Dischromic patches
    "watering_from_eyes": st.checkbox("Слезотечение", key="watering_from_eyes"),  # Watering from eyes
    "increased_appetite": st.checkbox("Повышенный аппетит", key="increased_appetite"),  # Increased appetite
    "polyuria": st.checkbox("Частое мочеиспускание", key="polyuria"),  # Polyuria
    "family_history": st.checkbox("Отягощенный семейный анамнез", key="family_history"),  # Family history
    "mucoid_sputum": st.checkbox("Мокрота прозрачно-белая", key="mucoid_sputum"),  # Mucoid sputum
    "rusty_sputum": st.checkbox("Ржавая мокрота", key="rusty_sputum"),  # Rusty sputum
    "lack_of_concentration": st.checkbox("Рассеянность", key="lack_of_concentration"),  # Lack of concentration
    "visual_disturbances": st.checkbox("Нарушения зрения", key="visual_disturbances"),  # Visual disturbances
    "receiving_blood_transfusion": st.checkbox("Было переливание крови", key="receiving_blood_transfusion"),  # Receiving blood transfusion
    "receiving_unsterile_injections": st.checkbox("Были нестерильные инъекции", key="receiving_unsterile_injections"),  # Receiving unsterile injections
    "coma": st.checkbox("Кома", key="coma"),  # Coma
    "stomach_bleeding": st.checkbox("Желудочное кровотечение", key="stomach_bleeding"),  # Stomach bleeding
    "distention_of_abdomen": st.checkbox("Вздутие живота", key="distention_of_abdomen"),  # Distention of abdomen
    "history_of_alcohol_consumption": st.checkbox("История употребления алкоголя", key="history_of_alcohol_consumption"),  # History of alcohol consumption
    "fluid_overload": st.checkbox("Перегрузка жидкостью", key="fluid_overload_two"),  # Fluid overload
    "blood_in_sputum": st.checkbox("Кровь в мокроте", key="blood_in_sputum"),  # Blood in sputum
    "prominent_veins_on_calf": st.checkbox("Выступающие вены на голени", key="prominent_veins_on_calf"),  # Prominent veins on calf
    "palpitations": st.checkbox("Ощущение сердцебиения", key="palpitations"),  # Palpitations
    "painful_walking": st.checkbox("Болезненная ходьба", key="painful_walking"),  # Painful walking
    "pus_filled_pimples": st.checkbox("Гнойные прыщи", key="pus_filled_pimples"),  # Pus-filled pimples
    "blackheads": st.checkbox("Черные точки", key="blackheads"),  # Blackheads
    "scurring": st.checkbox("Рубцевание", key="scurring"),  # Scarring
    "skin_peeling": st.checkbox("Шелушение кожи", key="skin_peeling"),  # Skin peeling
    "silver_like_dusting": st.checkbox("Серебряный налет", key="silver_like_dusting"),  # Silver-like
    "small_dents_in_nails": st.checkbox("Вмятины на ногтях", key="small_dents_in_nails"),  # Small dents in nails
    "inflammatory_nails": st.checkbox("Воспаление ногтей", key="inflammatory_nails"),  # Inflammatory nails
    "blister": st.checkbox("Волдыри", key="blister"),  #blister
    "red_sore_around_nose": st.checkbox("Красные высыпания вокруг носа", key="red_sore_around_nose"),  # Red sore around nose
    "yellow_crust_ooze": st.checkbox("Желтый экссудат", key="yellow_crust_ooze"),  # Yellow crust ooze
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
    st.write(f"{features}, length: {len(features)} \n{selected_symptoms}\n\n")
    prediction = loaded_model.predict([features])
    st.write("Прогноз:", prediction[0])
