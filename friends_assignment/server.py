from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friend')
@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', all_friends = friends)


@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (name, age, created_at) VALUES (:name, :age, NOW())"
    data = {
             'name': request.form['name'],
             'age':  request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')
@app.route('/friends/<friend_id>')
def show(friend_id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query, data)
    return render_template('index.html', one_friend=friends)
app.run(debug=True)