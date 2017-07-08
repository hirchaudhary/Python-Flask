from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
mysql = MySQLConnector(app,'mydb')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email', methods=['POST'])
def create():
    email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')    
    email = request.form['email']
    validation = True
    if not email_re.match(email):
        flash('Invalid Email')
        validation = False
    if validation:
        query = "INSERT INTO email (email, created_at) VALUES (:email, NOW())"
        data = {'email': email}
        mysql.query_db(query, data)
        flash('Successfully Added!')
        return redirect('/success')
    return redirect('/')

@app.route('/success')
def show():
    email = mysql.query_db("SELECT * FROM email")
    return render_template('success.html', email = email)
app.run(debug=True)