from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    personas = ["persona1", "Persona2", "Persona3"]
    cosas = ["Cosa1", "cosa2", "cosa3"]
    return render_template('index.html', personas=personas, cosas=cosas)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
