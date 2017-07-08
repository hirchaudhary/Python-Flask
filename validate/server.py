from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['Post'])
def process():
    name = request.form['name']
    error = None
    if len(name) == 0:
        error = "Can't be empty"
    else:
        flash("Hello", name)
        return redirect('/')
    return render_template('index.html', error = error)
app.run(debug=True)