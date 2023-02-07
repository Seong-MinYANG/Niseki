from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.0ps45en.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client["animals"]
animal = db["animal"]

import requests
from bs4 import BeautifulSoup
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/index", methods=["GET", "POST"])

def animals_post():

    if request.method == "POST":
        age = request.form['age']
        animal_type = request.form['animal_type']
        url = request.form['url']
        desc = request.form['desc']
        name = request.form['name']

        animal_data = {
            'name': name,
            'desc': desc,
            'animal_type': animal_type,
            'age': age,
            'url': url,
        }

        collection_name = determine_collection()
        collection = db[collection_name]
        collection.insert_one(animal_data)
        return "Animal stored in collection '{}'".format(collection_name)
    else:
        return render_template("index.html")

def determine_collection():
    animal_type = request.form['animal_type']
    if animal_type == "dogs":
        return "dogs"
    elif animal_type == "cats":
        return "cats"
    else:
        return "others"

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)