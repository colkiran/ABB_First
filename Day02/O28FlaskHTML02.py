
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<usrname>")
def home(usrname):
    return render_template("index01.html", username=usrname, content="For Loop.....")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
