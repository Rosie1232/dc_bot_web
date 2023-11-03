from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get():
    return render_template('get.html')

@app.route('/about')
def about():
    return render_template('/about.html')

app.run(debug=True)