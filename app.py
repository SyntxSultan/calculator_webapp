from flask import Flask, request, jsonify, render_template
from basic_calculator_function import basic_calculator

def create_app():
    # Create the app object
    app = Flask(__name__)

    # Define calculator
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/predict',methods=['POST'])
    def predict():

        a = request.form['a']
        b = request.form['b']
        operation = str(request.form['operation'])

        result = basic_calculator(a,b,operation)

        return render_template('index.html', prediction_text=str(result))
    return app

