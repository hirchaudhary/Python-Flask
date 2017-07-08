import random
from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "CVEDFVvvvvv"
@app.route('/')
def demo():
	  return render_template('index.html')

@app.route('/guess', methods=['POST'])
def forms():
	  session['rand'] = random.randint(1, 101)
	  session['num'] = int(request.form['num'])
	  session['res'] = ""
	  guess = session['num']
	  randnum = session['rand']
	  if guess < randnum:
	    	session['res'] = "Too Low!"
	  elif guess > randnum:
	       	session['res'] = "Too High!"
	  elif guess == randnum:
	    	session['res'] = "was the same number!"
	  return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
	session.pop('num')
	session.pop('rand')
	session.pop('res')
app.run(debug=True)
