
from flask import Flask, render_template,request
import pickle
import numpy as np
import big
#from datetime import datetime
app= Flask(__name__)

model=pickle.load(open('prop_tmax.pkl','rb'))
@app.route('/')
def hello_world():
    return render_template('web.html')


@app.route('/predict',methods=['POST','GET'])
def predict():
    date_input= request.form.get('thedate')
   # date_input= date_input.strftime('%F')
    predicition= big.predict_tmax(date_input)
    print(predicition)
    print("The Maximunm temperature is:")
    return predicition


if __name__ == '__main__':
     app.debug = True
     app.run()


