from flask import Flask, render_template
from data import varer,ukensmeny,kontakt


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meny')
def meny():
    return render_template('meny.html', ukensmeny=ukensmeny)

@app.route('/varer')
def vis_varer():
    return render_template('varer.html', varer=varer)

@app.route('/kontakter')
def kontakter():
    return render_template('kontakliste.html', kontakt=kontakt)

if __name__ == "__main__":
    app.run(debug=True)