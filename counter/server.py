
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = ':) :)'
@app.route('/')
def counter():
    try:
        session['counter'] += 1
        print counter
    except:
        session['counter'] = 1
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    session['counter'] += 1
    print counter
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)