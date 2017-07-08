from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = "Hi ;D:D"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/output', methods=['POST'])
def output():

    session["name"]        = request.form['name']
    session["location"]    = request.form['location']
    session["language"]    = request.form['language']
    session["description"] = request.form['description']
    return render_template("output.html")

app.run(host='192.168.1.5',port=5000,debug=True)