from flask import Flask,request,url_for,redirect,render_template
import pickle
import numpy as np


model = pickle.load(open('ForestModel.pickle','rb'))
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("forest_fire.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    # features = [int(x) for x in request.form.values()]
    # final = [np.array(features)]
    # print(features)
    # print(final)
    # prediction = model.predict(final)
    # output='{0:.{1}f}'.format(prediction[0][1], 2)
    
    lat = request.form.get("t1",type=float,default=0)
    lon = request.form.get("t2",type=float,default=0)
    bright = request.form.get("t3",type=float,default=0)
    satellite = request.form.get("t4",type=float,default=0)
    frp = request.form.get("t5",type=float,default=0)
    dayn = request.form.get("t6",type=float,default=0)
    type2 = request.form.get("t7",type=float,default=0)
    type3 = request.form.get("t8",type=float,default=0)
    scan = request.form.get("t9",type=float,default=0)
    year = request.form.get("t10",type=float,default=0)
    month = request.form.get("t11",type=float,default=0)
    day = request.form.get("t12",type=float,default=0)
    
    # features = [float(i) for i in request.form.values()]
    # Convert features to array
    lis = [[lat,lon,bright,satellite,frp,dayn,type2,type3,scan,year,month,day]]
    # a = np.empty(12)
    # for i in range(0,12):

    # array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(lis)
 
    output = prediction[0]
    print(output)

    if output> 50:
        return render_template('forest_fire.html',pred='Your Forest is in Danger.\nPercentage of fire occuring is {}%'.format(float(output)),bhai="danger")
    else:
        return render_template('forest_fire.html',pred='Your Forest is safe.\n Percentage of fire occuring is {}%'.format(float(output)),bhai="safe")

if __name__ == '__main__':
    app.run(debug=True)