import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# Load the model and scaler
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scaler   = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print("Received:", data)

    # Convert dict → array
    input_data = np.array(list(data.values())).reshape(1, -1)

    # Scale input
    scaled_data = scaler.transform(input_data)

    # Predict
    output = regmodel.predict(scaled_data)

    print("Prediction:", output[0])
    return jsonify({"prediction": float(output[0])})

@app.route('/predict', methods=['POST'])
def predict():
    # get a form to get the input features
    data =[float(x)for x in request.form.values()]
    final_input = scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output = regmodel.predict(final_input)[0]
    return render_template("home.html",prediction_text="The predicted price of the house is {}".format(output))


if __name__ == "__main__":
    app.run(debug=True)
