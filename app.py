from flask import Flask,render_template , request, jsonify
import pickle
import numpy as np
from meteostat import Stations, Daily, Point
from datetime import datetime

pune = Point(18.5204, 73.8567)
start = datetime(2023, 2, 15)
end = datetime(2023, 2, 15)
data = Daily(pune, start, end)
data = data.fetch()
data = data.fillna(0.0)


#for tavg
tavg_model = pickle.load(open('tavg.pkl', 'rb'))
tavg = tavg_model.predict(data.drop(['tavg'], axis=1))
print(tavg)

#for tmin
tmin_model = pickle.load(open('tmin.pkl', 'rb'))
tmin = tmin_model.predict(data.drop(['tmin'], axis=1))
print(tmin)

#for tmax
tmax_model = pickle.load(open('tmax.pkl', 'rb'))
tmax = tmax_model.predict(data.drop(['tmax'], axis=1))
print(tmax)


app = Flask(__name__)



@app.route("/")
def predict():
  values = [tavg[0], tmin[0], tmax[0]]
  return jsonify(values)

if __name__=='__main__':
  app.run(debug=True)