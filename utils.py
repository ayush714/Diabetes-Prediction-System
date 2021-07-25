import numpy as np 
import joblib 

def preprocessdata(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age): 
    test_data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]] 
    trained_model  = joblib.load('model.pkl') 
    prediction = trained_model.predict(test_data) 

    return prediction  



prediction = preprocessdata(6,148,72,35,0,33.6,0.627,50) 
print(prediction) 