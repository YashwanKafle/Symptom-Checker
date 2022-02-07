
import streamlit as st
import pickle
import numpy as np
from data import symptoms,features



def load_model():
    loaded_model = pickle.load(open("symptom_checker.pkl","rb"))
    return loaded_model

model = load_model()




st.title("Symptom Checker")

    
symptom1 = st.selectbox("Select your first symptom",symptoms)
symptom2 = st.selectbox("Select your second symptom",symptoms)
symptom3 = st.selectbox("Select your third symptom",symptoms)
symptom4 = st.selectbox("Select your fourth symptom",symptoms)
symptom5 = st.selectbox("Select your fifth symptom",symptoms)

    

submit = st.button("Submit")

    
if submit:
    if symptom1 !='none':
        features[symptom1] = 1
    if symptom2 !='none':
        features[symptom1] = 1
    if symptom3 !='none':
        features[symptom1] = 1
    if symptom4 !='none':
        features[symptom1] = 1    
    if symptom5 !='none':
        features[symptom1] = 1

    x = list(features.values())
    x = np.array([x])
    display  = model.predict(x)

    st.subheader(f"You might be suffering from {display[0]}")

    for keys in features:
        features[keys] = 0
        