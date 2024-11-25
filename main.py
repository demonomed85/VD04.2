from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films():
    return render_template("index.html")


@app.route("/dobronravov/")
def dobronravov():
    return render_template("dobronravov.html")

@app.route("/dobrynin/")
def dobrynin():
    return render_template("dobrynin.html")

@app.route("/koshmal/")
def koshmal():
    return render_template("koshmal.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run(debug=True)