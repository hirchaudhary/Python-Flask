
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def demo():
	return render_template('index.html')

@app.route('/ninja')
def contact():
	return render_template('ninja.html')
	
@app.route('/ninja/<color>')
def select(color):
	if color == "red":
		return render_template('Raphael.html')
	elif color == "orange":
		return render_template('Michelangalo.html')
	elif color == "blue":
		return render_template('Leonardo.html')
	elif color == "purple":
		return render_template('Donatello.html')
	else:
		return render_template('Notapril.html')
app.run(debug=True)
