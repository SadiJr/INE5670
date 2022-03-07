from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", number_loop=[1, 2], title="Isso é um título", username="User1")


@app.errorhandler(404)
def not_found(self):
    return "Errou"


app.run(port=8080, debug=True)