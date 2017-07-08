
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def demo():
	return render_template('main.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')
	
@app.route('/hello')
def hello():
	return render_template('hello.html')

app.run(debug=True)
