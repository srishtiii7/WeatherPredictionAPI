from flask import Flask, render_template, request
import pickle
app = Flask(__name__)


@app.route('/my-first-api', methods=['GET', 'POST'])

def home():
    if request.method == 'POST' :
        model = pickle.load(open('lr_model.pkl','rb'))
        user_input = request.form.get('size')
        prediction = model.predict([[user_input]])
        print(prediction)
    return render_template('project.html')
    
if __name__ == '__main__':
    app.run(debug=True)