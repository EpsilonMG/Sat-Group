from crypt import methods
from flask import Flask, render_template,request
import joblib
#from helpers.dummies import *
app=Flask(__name__)
model=joblib.load('models/model.h5')

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/recommend',methods=['GET'])
def recommend():
    all_data=request.args
    return all_data
   
   # return render_template('recommendation.html')



if __name__ == '__main__':
    app.run()