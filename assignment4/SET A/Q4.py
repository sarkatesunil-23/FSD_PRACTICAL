from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Welcome to Home Page"

@app.route('/student')
def student():
    return "Welcome Student"

@app.route('/faculty')
def faculty():
    return "Welcome Faculty"

if __name__ == '__main__':
    app.run(debug=True)