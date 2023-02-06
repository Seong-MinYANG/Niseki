from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient("mongodb+srv://test:sparta@cluster0.0ps45en.mongodb.net/?retryWrites=true&w=majority")
db = client["UserID"]
users = db["users"]

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/register", methods=["POST"])
def register():
    user_data = {
        "username": request.form.get("username"),
        "nickname": request.form.get("nickname"),
        "password": request.form.get("password"),
    }

    db.users.insert_one(user_data)

    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    movies_list = list(db.movies.find({},{'_id':False}))
    return jsonify({'movies':movies_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)