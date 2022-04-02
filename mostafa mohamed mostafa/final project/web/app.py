from flask import Flask,render_template,request
from helpers.helper import *
import joblib
app=Flask(__name__)

model=joblib.load('models\model.h5')
scaler=joblib.load('models\scaler.h5')
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict",methods=["GET"])
def predict():
    all_data=request.args
    PhysicalHealth=float(all_data["PhysicalHealth"])
    agecategory=all_data["agecategory"]
    alcoholdrinking=int(all_data["alcoholdrinking"])
    asthma=int(all_data["asthma"])
    bmi=float(all_data["bmi"])
    diabetic=int(all_data["diabetic"])
    diffwalking=int(all_data["diffwalking"])
    genhealth=all_data["genhealth"]
    kidneydisease=int(all_data["kidneydisease"])
    mentalhealth=float(all_data["mentalhealth"])
    physicalactivity=int(all_data["physicalactivity"])
    sex=int(all_data["sex"])
    skincancer=int(all_data["skincancer"])
    sleeptime=float(all_data["sleeptime"])
    smoke=int(all_data["smoke"])
    stroke=int(all_data["stroke"])
    data=[[bmi,smoke,alcoholdrinking,stroke,PhysicalHealth,mentalhealth,diffwalking,sex,diabetic,physicalactivity,sleeptime,asthma,kidneydisease,skincancer]+AgeCategory[agecategory]+GenHealth[genhealth]]
    data=scaler.transform(data)
    valu_predict=model.predict(data)
    

    return render_template("predict1.html",p=valu_predict)
    






if __name__=="__main__":
    app.run(debug=True)

           