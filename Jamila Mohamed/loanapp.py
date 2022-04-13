from flask import Flask,render_template,request
import joblib
from helpers.dummies import *

app=Flask(__name__)

model=joblib.load('models/loan_model.h5')
scaler=joblib.load('models/loan_scaler.h5')

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET'])
def predict():
    all_data=request.args
    income=float(all_data['income'])
    age=float(all_data['age'])
    experience=float(all_data['experience'])
    current_job_years=float(all_data['current_job_years'])
    current_house_years=float(all_data['current_house_years'])

    marital_status=all_data['marital_status']
    house_ownership=all_data['house_ownership']
    car_ownership=all_data['car_ownership']
    profession=all_data['profession']

    data=[income,age,experience,current_job_years,current_house_years]+marital_status_dummies[marital_status]+house_ownership_dummies[house_ownership]+car_ownership_dummies[car_ownership]+profession_dummies[profession]
    final_data=scaler.transform([data])
    pred=model.predict(final_data)[0]
    pred2=risk_flag_dummies[pred]
    return render_template('prediction.html',Risk_Flag=pred2)


if __name__=='__main__':
    app.run()