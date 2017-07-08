
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def demo():
	return render_template('index.html')

@app.route('/ninja')
def ninja():
	return render_template('ninja.html')

@app.route('/dojos')
def dojos():
	return render_template('dojos.html')

@app.route('/ninja',methods=['POST'])
def forms():
    name = request.form['name']
    about = request.form['about']
    return render_template('ninja.html', name=name, about=about)

app.run(debug=True)
#host='72.213.254.184', port=5000, 