
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('template.html', number_loop=[1], title="teste", username="test")


if __name__ == '__main__':
    app.run(debug=True)