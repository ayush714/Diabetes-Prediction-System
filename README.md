# Diabetes Prediction System 

This System is for checking, whether you have diabetes based on some inputs.
## Installation

You don't require any installation for this, you can go to the below website to start using it. 
Website:- https://diabetes-prediction-systems.herokuapp.com/ 

If you are developer and want to see and contribute, you can clone this repo using below command:- 


```bash
git clone https://github.com/ayush714/Diabetes-Prediction-System.git
```

## Inputs features:- 

- Pregnancies : You have to input how many number of a female got pregnant, if the user is male, kindly use 0 for that. 
- Glucose : In this feature you have to fill up your Glucose.
- BP ( Blood Pressure ) : The User have to fill BP 
- Skin Thickness  
- Insulin 
- BMI 
- Diabetes Pedigree Function 
- Age 

## Approach & Results 

I have used the following models, 

- **Decision Trees With Tuning**  
- **Random Forest with Extensive Tuning**
- **XGBoost** 
- **Catboost**  

So, I have decided to go with Catboost, because it is more robust, it is less prone to overfitting. The results are below after details about Evaluation.

I have used C-Index for Evaluation of the models, below is the formula for calculating C-Index:- 

cindex = concordant + 0.5 x ties / permissible 
- The c-index measures the discriminatory power of a risk score.
- A higher c-index indicates that the model's prediction is in agreement with the actual outcomes of a pair of patients.

**Results**:- 
'|    | Models         |\n|---:|:---------------|\n|  0 | Decision Trees |\n|  1 | Random Forest  |\n|  2 | XGboost        |\n|  3 | Catboost       |'



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
