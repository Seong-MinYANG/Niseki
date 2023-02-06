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
   return render_template('mypage.html')

@app.route("/mypage", methods=["POST"])
def mypage():

    animal_data = {
        "age": request.form.get("age"),
        "categories": request.form.get("categories"),
        "url": request.form.get("url"),
        "desc": request.form.get("desc"),
        "name": request.form.get("name"),
        "image": request.form.get("image"),
    }

    db.animal.insert_one(animal_data)

    return jsonify({'msg': '등록완료!'})

@app.route("/animals", methods=["GET"])
def animals_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)