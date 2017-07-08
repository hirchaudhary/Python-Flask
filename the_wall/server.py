from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
app = Flask(__name__)
app.secret_key = "ThisISSecret"
mysql = MySQLConnector(app,'wall')

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

	query = "SELECT * FROM users WHERE email= :email_exist"
	data = {
		'email_exist': email
	}
	e_check = mysql.query_db(query, data)

	if len(e_check) > 0:
		flash("Email already exist")
		validation = False
	if len(first_name) < 2:
		flash("Enter valid name")
		validation = False
	if len(last_name) < 2:
		flash("Enter valid last name")
		validation = False
	if len(email) < 5 or not email_re.match(email):
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
		query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
		data = {
			'first_name': request.form['first_name'],
			'last_name':  request.form['last_name'],
			'email': request.form['email'],
			'password': hash
		}
		user = mysql.query_db(query, data)
		session['user_id'] = user[0]['user_id']
		session['name'] = user[0]['first_name']
		flash("Registration successful")
		return redirect('/wall')
	return redirect('/')

@app.route('/login', methods=['Post'])
def login():
	email    = request.form['email']
	password = request.form['password']
	query = "SELECT * FROM users WHERE email= :email"
	data = {
		'email': request.form['email']
	}
	user = mysql.query_db(query, data)
	session['user_id'] = user[0]['user_id']
	session['name'] = user[0]['first_name']
	if len(user) < 1:
		flash("Email not exist")
	else:
		isHash = bcrypt.check_password_hash(user[0]['password'], password)
		if not isHash:
			flash("Password incorrect")
		else:
			return redirect('/wall')
	return redirect('/')

@app.route('/wall')
def welcome():
	messages = "SELECT * FROM users JOIN messages ON users.user_id = messages.users_id ORDER BY messages.created_at DESC"
	comment = "SELECT * FROM users JOIN comments ON users.user_id = comments.users_id ORDER BY comments.created_at DESC"
	messages = mysql.query_db(messages)
	comment = mysql.query_db(comment)
	return render_template('wall.html', messages = messages, comments = comment)

@app.route('/message', methods=['Post'])
def message():
	message = request.form['message']
	validation = True

	if len(message) < 1:
		flash("Please Give a message")
		validation = False
	if validation:
		user_id = session['user_id']
		query = "INSERT INTO messages (message, created_at, updated_at, users_id) VALUES (:message, NOW(), NOW(), :user_id)"
		data = {
			'message': request.form['message'],
			'user_id': user_id
		}
		mysql.query_db(query, data)
		return redirect('/wall')
	return redirect('/')

@app.route('/comment/<message_id>', methods=['Post'])
def comment(message_id):
	print message_id
	comment = request.form['comment']
	print comment
	print message
	validation = True
	if len(comment) < 1:
		flash("Please Give a comment")
		validation = False
	if validation:
		query = "INSERT INTO comments (comment, created_at, updated_at, users_id, messages_id) VALUES (:comment, NOW(), NOW(), :user_id, :message_id)"
		data = {
		'comment': request.form['comment'],
		'user_id': session['user_id'],
		'message_id': message_id
		}
		mysql.query_db(query, data)
		return redirect('/wall')
	return redirect('/')

@app.route('/logout')
def logout():
	session.pop('user_id')
	return redirect('/')

app.run(debug=True)
