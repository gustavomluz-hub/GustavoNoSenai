from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/inimigo')
def inimigo():
    return render_template('inimigo.html')

@app.route('/inimigo2')
def inimigo2():
    return render_template('inimigospt2.html')

if __name__ == '__main__':
    app.run(debug=True)
