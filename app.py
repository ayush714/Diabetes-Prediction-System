from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import html 
import utils 

app = Flask(__name__) 

@app.route('/') 
def home(): 
    return render_template('index.html') 

@app.route('/predict/', methods = ['GET', 'POST']) 
def predict():
    if request.method == 'POST': 
        Pregnancies	    = request.form.get('Pregnancies') 
        Glucose	        = request.form.get('Glucose') 
        BloodPressure	= request.form.get('BloodPressure')   
        SkinThickness	= request.form.get('SkinThickness') 
        Insulin	        = request.form.get('Insulin')
        BMI	            = request.form.get('BMI') 
        DiabetesPedigreeFunction	= request.form.get('DiabetesPedigreeFunction') 
        Age	            = request.form.get('Age')

    prediction = utils.preprocessdata(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    return render_template('predict.html', prediction = prediction) 


if __name__ == "__main__": 
    app.run(debug=True) 
