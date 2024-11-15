from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib  # Assuming your model is saved with joblib

app = Flask(__name__)

# Load your trained model
model = joblib.load('Predictor.ipynb')  # Update with your model path

# Route for the home page with the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and return prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    name = request.form['name']
    dob = request.form['dob']
    cutoff_mark = float(request.form['cutoff'])
    category = request.form['category']
    rank = int(request.form['rank'])

    # Prepare input data for prediction (adjust if needed)
    input_data = [[cutoff_mark, category, rank]]  # Adjust based on your model input

    # Get the top 5 eligible colleges (mock function here, replace with your actual function)
    prediction_result = model.predict(input_data)  # Replace with your prediction function
    
    # Render the output page with prediction results
    return render_template('output.html', name=name, result=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
