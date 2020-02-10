from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/groupes')
def groupes():
    return render_template("groupes.html")

@app.route('/modules')
def modules():
    return render_template("modules.html")

@app.route('/profs')
def profs():
    return render_template("profs.html")

@app.route('/evaluations')
def evaluations():
    return render_template("evaluations.html")

@app.route('/connexion')
def connexion():
    return render_template("connexion.html")

@app.route('/table')
def table():
    return render_template("table.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/charts')
def charts():
    return render_template("charts.html")

if __name__=='__main__':
    app.run(debug=True)
