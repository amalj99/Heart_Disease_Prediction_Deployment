# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 16:01:58 2020

@author: Amal Jain
"""

import streamlit as st
import pandas as pd
import pickle
from PIL import Image

pickle_in=open('model.pk', 'rb')
classifier=pickle.load(pickle_in)

image=Image.open('jpeg1.jpg')
st.image(image,width=500)

st.title('Heart Disease Prediction')
 
selectbox=st.sidebar.selectbox('Select operation to be performed',['Enter values for prediction'
                                                                   ,'View training dataset','View dataset analysis'])
if selectbox == 'Enter values for prediction':
    
    st.subheader("Enter the appropriate values for each field and press 'Predict' to get the result.")
    
    age=st.number_input('Age', min_value= 1 , max_value = 100 , value =20)
    
    sex=st.selectbox('Sex',['Male','Female'])
    if sex=='Male':
        sex=1
    else:
        sex=0
    
    cp=st.selectbox('Chest Pain Type:',['Asymptomatic','Atypical Angina','Non-Anginal pain','Typical Angina'])
    if cp=='Asymptomatic':
        cp=0
    elif cp=='Atypical Angina':
        cp=1
    elif cp=='Non-Anginal pain':
        cp=2
    else:
        cp=3
    
    trestbps=st.number_input('Resting Blood Pressure', min_value=30 , max_value=250, value=120)
    
    chol=st.number_input('Serum Cholestrol(mg/dl)', min_value = 50, max_value = 450, value= 200)
    
    fbs=st.selectbox('Fasting Blood Sugar', ['<120 mg/dl','>120 mg/dl'])
    if fbs=='<120 mg/dl':
        fbs=0
    else:
        fbs=1
    
    restcg=st.selectbox('Resting electrocardiographic results:', ['Normal'
        ,'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)'
        ,'Showing probable or definite left ventricular hypertrophy by Estes criteria'])
    if restcg=='Normal':
        restcg=0
    elif restcg=='Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)':
        restcg=1
    else:
        restcg=2
    
    thalach= st.number_input('Maximum heart rate achieved', min_value= 50, max_value=240, value=150)
    
    exang=st.selectbox('Exercise Induced Angina',['No','Yes'])
    if exang=='No':
        exang=0
    else:
        exang=1
   
    
    oldpeak=st.slider('ST depression induced by exercise relative to rest', min_value=float(0)
                            ,max_value=float(5),value=float(1))
    
    slope=st.selectbox('The slope of the peak exercise ST segment', ['Upsloping','Flat','Downsloping'])
    if slope=='Upsloping':
        slope=1
    elif slope=='Flat':
        slope=2
    else:
        slope=3
    
    ca=st.selectbox('number of major vessels (0-3) colored by flourosopy',[0,1,2,3])
    
    tha=st.selectbox('Thalium Stress Test Result',['Fixed defect','Normal','Reversible defect'])
    if tha=='Fixed defect':
        tha=1
    elif tha=='Normal':
        tha=2
    else:
        tha=3
    
    input_dict={'age':age, 'sex': sex, 'cp':cp, 'trestbps':trestbps, 'chol':chol, 'fbs':fbs, 'restcg':restcg, 
                'thalach':thalach, 'exang':exang, 'oldpeak':oldpeak, 'slope':slope, 'ca':ca, 'tha':tha}
    
    input_df=pd.DataFrame([input_dict])
    
    if st.button("Predict"):
        output=classifier.predict(input_df)
        prob=classifier.predict_proba(input_df)
        if int(output)==0:
            st.success('Congratulations! The probability of you NOT having a heart disease is {}%'.format(round(prob[0][0]*100,2)))
        else:
            st.success('The probability of you having a heart disease is {}%, please consult a doctor.'.format(round(prob[0][1]*100)))
    
if selectbox == 'View training dataset':
    data=pd.read_csv('heart_disease_data_cleaned.csv')
    st.dataframe(data)

if selectbox == 'View dataset analysis':
    graph=st.selectbox('Select graph to be displayed',['Heart Disease frequency vs Sex','Heart Disease frequency vs Age'
                                                 ,'Heart Disease frequency vs Chest pain type'])
    if graph == 'Heart Disease frequency vs Sex':
        image2=Image.open('disease vs sex.png')
        st.image(image2, width=800)
    if graph == 'Heart Disease frequency vs Age':
        image3=Image.open('disease vs age.png')
        st.image(image3,width=800)
    if graph == 'Heart Disease frequency vs Chest pain type':
        image4=Image.open('disease vs pain type.png')
        st.image(image4,width=800)
        

