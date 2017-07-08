
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def demo():
	return render_template('index.html')

@app.route('/process',methods=['POST'])
def forms():
    name = request.form['name']
    return render_template('process.html', name=name)

app.run(debug=True)
#host='72.213.254.184', port=5000