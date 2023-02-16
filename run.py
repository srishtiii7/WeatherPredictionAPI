from flask import Flask, render_template, request
import pickle 

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])

def home():
    if request.method== 'POST':
        model = pickle.load(open('rr_model.pkl','rb'))
        user_input = request.form.get('thedate')
        prediction = model.predict([[user_input]])
        
    return render_template('web.html', predictions = prediction)
    
if __name__ == '__main__':
    app.run(debug=True)