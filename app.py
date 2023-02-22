from flask import Flask, request, render_template, jsonify
import pickle #To use ML model which is saved as a pickle file used during inference
import pandas as pd
import requests

app = Flask(__name__)

# Basic application endpoints available in the web application
@app.route("/", methods = ["GET", "POST"])
def home():
    AuthorName = "Bishwas Praveen"
    return render_template("home.html", user=AuthorName)

@app.route("/single-sample", methods = ["GET", "POST"])
def singleSample():
    return render_template("single-sample.html")

@app.route("/batch-processing", methods = ["GET", "POST"])
def batchProcesing():
    return render_template("batch-processing.html")

# This is the endpoint which processes the AJAX request from the webpage upon button click and generates the clasification results from the ML application deployed on the MLFlow server for a single sample
@app.route("/evaluateSingleSampleMode", methods = ["GET", "POST"])
def evaluateSingleSampleMode():
    sl = request.form["sepallength"]
    sw = request.form["sepalwidth"]
    pl = request.form["petallength"]
    pw = request.form["petalwidth"]
    inputList = [float(sl), float(sw), float(pl), float(pw)]
    print (inputList)
    inference_request = {
        "data" : [inputList]
    }
    #This is the server endpoint of MLFlow which is used to predict the results for the given input
    endpoint = "http://localhost:1234/invocations"
    response = requests.post(endpoint, json=inference_request)
    print (response.text)
    return str(response.text.strip(' "[]'))

# This is the endpoint which processes the AJAX request from the webpage upon button click and generates the clasification results from the ML application deployed on the MLFlow server for batch processing
@app.route("/evaluateBatchProcessing", methods = ["GET", "POST"])
def evaluateBatchProcessing():
    uploaded_file = request.files['file']
    df = pd.read_csv(uploaded_file)
    lst = df.values.tolist()
    inference_request = {
        "data" : lst
    }
    endpoint = "http://localhost:1234/invocations"
    response = requests.post(endpoint, json = inference_request)
    # Parse the response and format it as an array of objects
    results = []
    for i, prediction in enumerate(response.json()):
        results.append({'sample_index': i + 1, 'predicted_class': prediction})
    # Return the results as a JSON array
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug = True)