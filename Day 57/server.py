from flask import Flask, render_template
import random 
import datetime
from datetime import datetime
import requests

 

app = Flask(__name__)
name = 1

@app.route(f'/guess/<name>')
def home(name):
    response_gender = requests.get(f"https://gender-api.com/get?name={name}&key=RjKRRD8q5C7v7w75MYVHjAJK9HhPa8FaraQN")
    gender_dict = response_gender.json() # This method is convenient when the API returns JSON


    response_agify = requests.get(f"https://api.agify.io?name={name}")
    agify_dict = response_agify.json() # This method is convenient when the API returns JSON


    gender = gender_dict['gender']
    age = agify_dict['age']
   
    return render_template("index.html", name=name, gender=gender, age=age)

@app.route(f'/blog')
def home(name):
    response_gender = requests.get(f"https://gender-api.com/get?name={name}&key=RjKRRD8q5C7v7w75MYVHjAJK9HhPa8FaraQN")
    gender_dict = response_gender.json() # This method is convenient when the API returns JSON


    response_agify = requests.get(f"https://api.agify.io?name={name}")
    agify_dict = response_agify.json() # This method is convenient when the API returns JSON


    gender = gender_dict['gender']
    age = agify_dict['age']
   
    return render_template("index.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)