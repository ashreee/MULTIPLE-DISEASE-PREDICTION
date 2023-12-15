import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

#diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

#parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

#breast_cancer_data_model = pickle.load(open('breast_cancer_data_model.sav', 'rb'))

diabetes_model = pickle.load(open("C:/Users/fathi/OneDrive/Desktop/MULTIPLE DISEASE PREDICTION/sav files/diabetes_model.sav",'rb'))
heart_disease_model = pickle.load(open("C:/Users/fathi/OneDrive/Desktop/MULTIPLE DISEASE PREDICTION/sav files/heart_disease_model.sav",'rb'))
breast_cancer_model = pickle.load(open("C:/Users/fathi/OneDrive/Desktop/MULTIPLE DISEASE PREDICTION/sav files/breast_cancer_model .sav", 'rb'))




# sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Attack Prediction',
                           'Breast Cancer Prediciton',
                           ],
                          icons=['droplet','activity','gender-female'],
                          default_index=0)
    st.markdown("""
<style>
    .header {
        background-image: linear-gradient(to right, #F7B2B2,#CCDAF5,#F0FFF0 );

        color: white;
        padding: 10px;
        text-align: center;
        border-radius: 5px;
    }
    .css-7lhw2n p{
    font-size: large;
    color: rgb(49, 51, 63);
    display: flex;
    visibility: visible;
    margin-bottom: 0.25rem;
    height: auto;
    min-height: 1.5rem;
    vertical-align: middle;
    flex-direction: row;
    -webkit-box-align: center;
    align-items: center;
}
            
                    .st-b8 {
                           max-width: 50%;
                text-align:center;
                           }
                
                .css-15zwcoi{
                background-color: rgba(247,178,178); 
                color: white; 
                border: 2px solid #F7B2B2;
                }
                .css-15zwcoi:hover{
                border-color:grey;
                color:black;
                background-color:white;
                
                }
                .css-15zwcoi:focus:not(:active){
                background-color: rgba(247,178,178); 
                color: white; 
                border: 2px solid #F7B2B2;
                }
                .css-1wfzc1r {
                margin:center;
                }
                body,p{
                text-align:center;
                }
                .css-1hynsf2{
                text-align:center;
                position:relative;
                }
               #element-container{
                  text-align:center;
               }


                
                
</style>
""", unsafe_allow_html=True)
    
# Header
st.markdown('<div class="header"><h1>Disease Prediction System</h1></div>', unsafe_allow_html=True)
    
    # Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')
    
    # getting the input data from the user
    
    

    Pregnancies = st.text_input('Number of Pregnancies (Ex: 0,17)')
    
    Glucose = st.text_input('Glucose Level (Ex: 0,163)')
    
    
    BloodPressure = st.text_input('Blood Pressure value (Ex: 0,122)')
    
   
    SkinThickness = st.text_input('Skin Thickness value (Ex: 0,99)')
    
   
    Insulin = st.text_input('Insulin Level (Ex: 0,846)')
    
    
    BMI = st.text_input('BMI value (Ex: 0,67.1)')
    
    
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree value (Ex: 0.078,2.42)')
    
    
    Age = st.text_input('Age of the Person (Ex: 21,81)')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, 
                                                   SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person may have diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Attack Prediction'):
    
    # page title
    st.title('Heart Attack Prediction')
    
   
    
  
    age = st.number_input('Age (Ex: 29,77)')
        
    
    sex = st.number_input('Sex (Ex: 0,1)')
        
   
    cp = st.number_input('Chest Pain types (Ex: 0,3)')
        
    
    trestbps = st.number_input('Resting Blood Pressure (Ex: 94,200)')
        
   
    chol = st.number_input('Serum Cholestoral in mg/dl (Ex: 126,564)')
        
    
    fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (Ex: 0,1)')
        
    
    restecg = st.number_input('Resting Electrocardiographic results (Ex: 0,2)')
        
    
    thalach = st.number_input('Maximum Heart Rate achieved (Ex: 71,202)')
        
    
    exang = st.number_input('Exercise Induced Angina (Ex: 0,1)')
        
   
    oldpeak = st.number_input('ST depression induced by exercise (Ex: 0,6.2)')
        
    
    slope = st.number_input('Slope of the peak exercise ST segment (Ex: 0,2)')
        
    
    ca = st.number_input('Major vessels colored by flourosopy (Ex: 0,4)')
        
    
    thal = st.number_input('thal:0=normal;1=fixed defect;2=reversable defect (Ex:0,3)')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol,
                                                         fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'This person most likely to have Heart Attack'
        else:
          heart_diagnosis = 'Theis person less likely to have Heart Attack'
        
    st.success(heart_diagnosis)
        
      
    


# Breast Cancer Prediction Page
if (selected == "Breast Cancer Prediciton"):
    
    # page title
    st.title("Breast Cancer Prediciton")
    
    
    radius_mean = st.number_input('Radius of Lobes (Ex:6.98,28.1)')
        
    
    texture_mean = st.number_input('Mean of Surface Texture (Ex: 9.71,39.3)')
        
    
    
    perimeter_mean = st.number_input('Outer Perimeter of Lobes (Ex: 43.8,189)')
        
    
    area_mean = st.number_input('Mean Area of Lobes (Ex: 144,2500)')
        
    
    smoothness_mean = st.number_input('Mean of Smoothness Levels (Ex: 0.05,0.16)')
        
    
    compactness_mean = st.number_input('Mean of Compactness (Ex: 0.02,0.35)')
        
    
    concavity_mean = st.number_input('Mean of Concavity (Ex: 0,0.43)')
        
    
    concave_points_mean = st.number_input('Mean of Cocave Points (Ex: 0,0.2)')
        
    
    symmetry_mean = st.number_input('Mean of Symmetry (Ex: 0.11,0.3)')
        
    
    fractal_dimension_mean = st.number_input('Mean of Fractal Dimension (Ex: 0.05,0.1)')
        
    
    radius_se = st.number_input('SE of Radius (Ex: 0.11,2.87)')
        
    
    texture_se = st.number_input('SE of Texture (Ex: 0.36,4.88)')
        
    
    perimeter_se = st.number_input('Perimeter of SE (Ex: 0.76,22)')
        
    
    area_se = st.number_input('Area of SE (Ex: 6.8,542)')
        
    
    smoothness_se = st.number_input('SE of Smoothness (Ex: 0,0.03)')
        
    
    compactness_se = st.number_input('SE of compactness (Ex: 0,0.14)')
        
    
    concavity_se = st.number_input('SEE of concavity (Ex: 0,0.4)')
        
    
    concave_points_se = st.number_input('SE of concave points (Ex: 0,0.05)')
        
    
    symmetry_se = st.number_input('SE of symmetry (Ex: 0.01,0.08)')
        
    
    fractal_dimension_se = st.number_input('SE of Fractal Dimension (Ex: 0,0.03)')
        
    
    radius_worst = st.number_input('Worst Radius (Ex: 7.93,36)')
        
    
    texture_worst = st.number_input('Worst Texture (Ex: 12,49.5)')
    
    
    perimeter_worst = st.number_input('Worst Perimeter (Ex: 50.4,251)')
        
    
    area_worst = st.number_input('Worst Area (Ex: 185,4250)')
            
    
    smoothness_worst = st.number_input('Worst Smoothness (Ex: 0.07,0.22)')
                
    
    compactness_worst = st.number_input('Worse Compactness (Ex: 0.03,1.06)')
                    
    
    concavity_worst = st.number_input('Worst Concavity (Ex: 0,1.25)')
                        
    
    concave_points_worst = st.number_input('Worst Concave Points (Ex: 0,0.29)')
                            
    
    symmetry_worst = st.number_input('Worst Symmetry (Ex: 0.16,0.66)')
                                
    
    fractal_dimension_worst = st.number_input('Worst Fractal Dimension (Ex: 0.06,0.21)')
        
    
    
    # code for Prediction
    Breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        Breast_cancer_prediction =breast_cancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean,
                                                           smoothness_mean, compactness_mean, concavity_mean,concave_points_mean,
                                                           symmetry_mean,fractal_dimension_mean,
                                                           radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,
                                                           concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,
                                                           radius_worst,texture_worst,perimeter_worst,area_worst,
                                                           smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,
                                                           symmetry_worst,fractal_dimension_worst]])                          
        
        if (Breast_cancer_prediction[0] == 0):
          Breast_cancer_diagnosis = "This person may have malignant (cancerous) breast."
        else:
          Breast_cancer_diagnosis = "This person does not have malignant(cancerous) breast."
        
    st.success(Breast_cancer_diagnosis)



        
           

    




  