from flask import Flask,jsonify, request
from prediction import get_prediction

app = Flask(__name__)

@app.route("/predict-digit", methods=["POST"])
def predict_data():
   image = request.files.get("digit")
   prediction = get_prediction(image)
   return jsonify({
       "prediction" : prediction
   }),200
    

if (__name__ == "__main__"):
    app.run(debug=True)

"""from flask import Flask, app
from requests import request
from flask.json import jsonify

tasks = [
    {
        'id':1,
        'title':'my books',
        'description':'chemistry, physics, Biology',
        'done':False
    }
]
@app.route("/add-data",methods = ["POST"])
def  add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Please provide data',
        },400)

if (__name__ == "__main__"):
    app.run(debug= True)
    """