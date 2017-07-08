from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
app = Flask(__name__)
app.secret_key = "ThisISSecret"
mysql = MySQLConnector(app,'registration')

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['Post'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    validation = True
    if len(first_name) < 2:
        flash("Enter valid name")
        validation = False
    if len(last_name) < 2:
        flash("Enter valid last name")
        validation = False
    if not email_re.match(email):
        flash("Enter valid email")
        validation = False
    if len(password) < 8:
        flash("Enter valid password")
        validation = False
    if confirm_password != password:
        flash("Password must be same")
        validation = False
    if validation:
        hash = bcrypt.generate_password_hash(password)
        query = "INSERT INTO user (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
                'first_name': request.form['first_name'],
                'last_name':  request.form['last_name'],
                'email': request.form['email'],
                'password': hash
        }
        mysql.query_db(query, data)
        flash("Registration successful")
        return redirect('/welcome')
    return redirect('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/success', methods=['Post'])
def success():
    email    = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM user WHERE email= :email"
    data = {
                'email': request.form['email'],
            }
    user = mysql.query_db(query, data)
    if len(user) < 1:
        flash("Email not exist")
    else:
        isHash = bcrypt.check_password_hash(user[0]['password'], password)
        if not isHash:
            flash("Password incorrect")
        else:
            session['name'] = user[0]['first_name']
            return redirect('/welcome')
    return redirect('/login')

@app.route('/welcome')
def welcome():
    return render_template('success.html')

app.run(debug=True)
