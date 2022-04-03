from flask import Flask,render_template,request
import joblib
from helpers.dummies import *

app= Flask(__name__)

model=joblib.load('models/model_new.h5')
scaler=joblib.load('models/scaler_new.h5')

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET'])
def predict():
    all_data=request.args
    beds=int(all_data['beds'])
    baths=int(all_data['baths'])
    sqfeet=float(all_data['sqfeet'])
    cats_allowed=all_data['cats_allowed']
    dogs_allowed=all_data['dogs_allowed']
    wheelchair_access=all_data['wheelchair_access']
    smoking_allowed=all_data['smoking_allowed']
    comes_furnished=all_data['comes_furnished']
    lat=float(all_data['lat'])
    long=float(all_data['long'])
    
    type=all_data['type']
    laundry_options=all_data['laundry_options']
    parking_options=all_data['parking_options']



    data=[sqfeet,beds,baths,cats_allowed,dogs_allowed,smoking_allowed,wheelchair_access,comes_furnished,lat,long]+type_dummies[type]+laundry_options_dummies[laundry_options]+parking_options_dummies[parking_options]
    data=scaler.transform([data])
    pred=model.predict(data)


    return render_template('prediction.html',price=pred)







if __name__=='__main__':
    app.run()
