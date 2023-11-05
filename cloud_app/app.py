
import numpy as np
import joblib

from flask import Flask, request, jsonify

def predict_single(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]

model = joblib.load('rf_modelv1.joblib')
dv = joblib.load('dv.joblib')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():

    threshold = 0.14944631791961446
    patient = request.get_json()

    prediction = predict_single(patient, dv, model)
    has_diabetes = prediction >= threshold
    
    result = {
        'diabetes_probability': float(prediction),
        'has_diabetes': bool(has_diabetes),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
    #, host='0.0.0.0', port=9696
