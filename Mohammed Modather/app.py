from flask import Flask,render_template,request
import joblib
from helpers.dummies import *

app=Flask(__name__)

model=joblib.load('models/model1.h5')
scaler=joblib.load('models/scalerr.h5')
pca=joblib.load('models/pca.h5')

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET'])
def predict():
    all_data=request.args
    
    rev_mean=float(all_data['rev_mean'])
    totmrc_mean=float(all_data['totmrc_mean'])
    da_mean=float(all_data['da_mean'])
    ovrmou_mean=float(all_data['ovrmou_mean'])
    ovrrev_mean=float(all_data['ovrrev_mean'])
    datovr_mean=float(all_data['datovr_mean'])
    roam_mean=float(all_data['roam_mean'])
    change_mou=float(all_data['change_mou']) 
    drop_dat_mean=float(all_data['drop_dat_mean'])
    blck_vce_mean=float(all_data['blck_vce_mean'])
    blck_dat_mean=float(all_data['blck_dat_mean'])
    unan_vce_mean=float(all_data['unan_vce_mean'])
    unan_dat_mean=float(all_data['unan_dat_mean'])
    recv_vce_mean=float(all_data['recv_vce_mean'])
    comp_vce_mean=float(all_data['comp_vce_mean'])
    comp_dat_mean=float(all_data['comp_dat_mean'])
    custcare_mean=float(all_data['custcare_mean'])
    inonemin_mean=float(all_data['inonemin_mean'])
    threeway_mean=float(all_data['threeway_mean'])
    mou_cvce_mean=float(all_data['mou_cvce_mean'])
    mou_cdat_mean=float(all_data['mou_cdat_mean'])
    mou_rvce_mean=float(all_data['mou_rvce_mean'])
    owylis_vce_mean=float(all_data['owylis_vce_mean'])
    mouowylisv_mean=float(all_data['mouowylisv_mean'])
    iwylis_vce_mean=float(all_data['iwylis_vce_mean'])
    peak_vce_mean=float(all_data['peak_vce_mean'])
    peak_dat_mean=float(all_data['peak_dat_mean']) 
    mou_peav_mean=float(all_data['mou_peav_mean'])
    mou_pead_mean=float(all_data['mou_pead_mean'])
    opk_vce_mean=float(all_data['opk_vce_mean'])
    opk_dat_mean=float(all_data['opk_dat_mean'])
    mou_opkv_mean=float(all_data['mou_opkv_mean'])
    mou_opkd_mean=float(all_data['mou_opkd_mean']) 
    drop_blk_mean=float(all_data['drop_blk_mean'])
    complete_mean=float(all_data['complete_mean']) 
    callfwd_mean=float(all_data['callfwd_mean'])
    callwait_mean=float(all_data['callwait_mean'])
    months=int(all_data['months'])
    totcalls=int(all_data['totcalls'])
    totmou=float(all_data['totmou']) 
    totrev=float(all_data['totrev'])
    adjrev=float(all_data['adjrev'])
    adjmou=float(all_data['adjmou'])
    adjqty=float(all_data['adjqty'])
    avgrev=float(all_data['avgrev'])
    avgmou=float(all_data['avgmou'])
    avgqty=float(all_data['avgqty'])
    avg3mou=int(all_data['avg3mou'])
    avg3qty=int(all_data['avg3qty'])
    avg3rev=int(all_data['avg3rev']) 
    avg6mou=float(all_data['avg6mou']) 
    avg6qty=float(all_data['avg6qty']) 
    avg6rev=float(all_data['avg6rev']) 
    phones=float(all_data['phones']) 
    income=float(all_data['income'])

    creditcd=all_data['creditcd']
    area=all_data['area']

    data=[rev_mean,totmrc_mean,da_mean,ovrmou_mean,ovrrev_mean,
    datovr_mean,roam_mean,change_mou,drop_dat_mean,blck_vce_mean,blck_dat_mean,unan_vce_mean
    ,unan_dat_mean,recv_vce_mean,comp_vce_mean,comp_dat_mean,custcare_mean,inonemin_mean,threeway_mean
    ,mou_cvce_mean,mou_cdat_mean,mou_rvce_mean,owylis_vce_mean,mouowylisv_mean,iwylis_vce_mean,peak_vce_mean
    ,peak_dat_mean,mou_peav_mean,mou_pead_mean,opk_vce_mean,opk_dat_mean,mou_opkv_mean,mou_opkd_mean,drop_blk_mean
    ,complete_mean ,callfwd_mean,callwait_mean,months,totcalls,totmou ,totrev,adjrev,adjmou,adjqty
    ,avgrev,avgmou,avgqty,avg3mou,avg3qty,avg3rev,avg6mou,avg6qty,avg6rev
    ,phones,income]+creditcd_dummies[creditcd]+area_dummies[area]

    
    data=scaler.transform([data])
    data=pca.transform([data])
    return str(data)
    #data_final=[data[0:5]+data[6]+data[11]+data[16]+data[17]]
    #pred=model.predict(data_final)[0]
    #pred2=churn_dummies[pred]

    #return render_template('prediction.html',churn=pred2)








if __name__=='__main__':
    app.run()