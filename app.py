# Ref: https://github.com/bhavaniravi/rasa-site-bot
from decimal import Decimal
from flask import Flask
from flask import render_template,jsonify,request
import requests
import webbrowser
# from models import *
from engine import *
import random


app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def hello_world():
    return render_template('home.html')

get_random_response = lambda intent:random.choice(intent_response_dict[intent])

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      if request.form["submit"] == "AM EDPI":
        return render_template("am_edpi.html")  
      elif request.form["submit"] == "WM EDPI":
        return render_template("wm_edpi.html")
      else:
        return render_template('home.html')

@app.route('/chat',methods=['POST','GET'])
def chat():
    try:       
        user_message = request.form["text"]
        response = requests.get("http://localhost:5000/parse",params={"q":user_message})
        response = response.json()

        entities = response.get("entities")
        topresponse = response["topScoringIntent"]
        intent = topresponse.get("intent")
        score = topresponse.get("score")
        if Decimal(score) < 0.50:
            print(" ^^^^^^^^^^^^ Low Confidence ^^^^^^^^^^^^",Decimal(score))        
        print(response)        
        print("Intent {}, Entities {}".format(intent,entities))
        
        if intent == "edpi_faq":
            response_text = edpi_faq(entities)
        elif intent == "entitlements_info":
            print('OK inside entitlements_info')
            response_text = entitlements_info(entities)
        elif intent == "intro":
            response_text = get_random_response(intent)
        elif intent == "greet":
            response_text = get_random_response(intent)
        elif intent == "goodbye":
            response_text = get_random_response(intent)
        elif intent == "affirm":
            response_text = get_random_response(intent)
        else:
            response_text = "Sorry I am not trained to do that yet..."

        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)