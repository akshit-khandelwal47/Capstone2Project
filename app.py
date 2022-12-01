from flask import Flask,request,url_for,redirect,render_template
import pickle
import numpy as np


model = pickle.load(open('ForestModelOld.pickle','rb'))
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
    
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)
 
    output = prediction

    if output>str(0.5):
        return render_template('forest_fire.html',pred='Your Forest is in Danger.\nPercentage of fire occuring is {}%'.format(float(output)*100),bhai="danger")
    else:
        return render_template('forest_fire.html',pred='Your Forest is safe.\n Percentage of fire occuring is {}%'.format(float(output)*100),bhai="safe")

if __name__ == '__main__':
    app.run(debug=True)