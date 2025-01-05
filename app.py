import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Prediction of Disease Outbreaks",layout="wide",page_icon="medical-team_4807695.png")
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f'{working_dir}\saved_Model\diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open(f'{working_dir}\saved_Model\heart_disease_model1.sav','rb'))
parkinson_disease_model = pickle.load(open(f'{working_dir}\saved_Model\parkinson_model.sav','rb'))
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreaks System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity','heart','person'],
                           default_index=0)
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')
    col1,col2,col3 =st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,
                      DiabetesPedigreeFunction,Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is not Diabetic'
    st.success(diab_diagnosis)
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')
    col1,col2,col3 =st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain value')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('serum cholestrol in mg/dl')
    with col3:
        fbs = st.text_input('fasting blood sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic result')
    with col2:
        thalach = st.text_input('Maximum heart Rate Achieved')
    with col3:
        exang = st.text_input('Excercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by excercise')
    with col2:
        slope = st.text_input('Slope of the peak excercise ST segment')
    with col3:
        ca = st.text_input('Major vessel colored by flourosopy')
    with col1:
        thal = st.text_input('thal:0 = normal;1 = fixed defect; 2 = reversable defect')
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having Heart disease'
        else:
            heart_diagnosis = 'The person is not having Heart disease'
    st.success(heart_diagnosis)
if selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction Using ML")
    col1,col2,col3,col4,col5 =st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        rap = st.text_input('MDVP:RAP')
    with col2:
        ppq = st.text_input('MDVP:PPQ')
    with col3:
        ddp = st.text_input('Jitter:DDP')
    with col4:
        shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        apq3 = st.text_input('Shimmer:APQ3')
    with col2:
        apq5 = st.text_input('Shimmer:APQ5')
    with col3:
        apq = st.text_input('MDVP:APQ')
    with col4:
        shimmer_dda = st.text_input('Shimmer:DDA')
    with col5:
        nhr = st.text_input('NHR')
    with col1:
        hnr = st.text_input('HNR')
    with col2:
        rpde = st.text_input('RPDE')
    with col3:
        dfa = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        d2 = st.text_input('D2')
    with col2:
        ppe = st.text_input('PPE')
    parkinsons_diagnosis = ''
    if st.button('Parkinson Disease Test Result'):
        user_input = [fo,fhi,flo,jitter_percent,jitter_abs,rap,ppq,ddp,shimmer,
                      shimmer_db,apq3,apq5,apq,shimmer_dda,nhr,hnr,rpde,dfa,
                      spread1,spread2,d2,ppe]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinson_disease_model.predict([user_input])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = 'The person has parkinson disease'
        else:
            parkinsons_diagnosis = 'The person does not have parkinson disease'
    st.success(parkinsons_diagnosis)
    

        
