
from flask import Flask,render_template,request
import joblib
from helpers1.new_dummies import *
model=joblib.load('models/model.h5')
scaler=joblib.load('models/scaler.h5')
feature=joblib.load('models/features.h5')
app=Flask(__name__)



@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/predict',methods=['GET'])
def predict():
    all_data=request.args
    BMI=int(all_data['BMI'])
    AgeCategory=all_data['AgeCategory']
    AlcoholDrinking=all_data['AlcoholDrinking']
    Diabetic=all_data['Diabetic']
    GenHealth=all_data['GenHealth']
    
    PhysicalActivity=all_data['PhysicalActivity']
    Smoking=all_data['Smoking']
    
    Sex=all_data['Sex']
    Race=all_data['Race']
    l=['Your heart is OK','You may have heart problems,please confirm with clinical investigations']
    data=[BMI]+Smoking_dummies[Smoking]+AlcoholDrinking_dummies[AlcoholDrinking]+Sex_dummies[Sex]+AgeCategory_dummies[AgeCategory]+Race_dummies[Race]+Diabetic_dummies[Diabetic]+PhysicalActivity_dummies[PhysicalActivity]+GenHealth_dummies[GenHealth]
    data=scaler.transform([data])
    pred=model.predict(data)
    pred=l[int(pred)]
    return render_template('prediction.html',prediction=pred)

if __name__=='__main__':
    app.run()