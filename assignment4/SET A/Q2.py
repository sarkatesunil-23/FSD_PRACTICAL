from flask import Flask

app = Flask(__name__)

@app.route('/contact')
def contact():
    return "This is a contact page"

@app.route('/services')
def services():
    return "This is a Services page"

if __name__ == '__main__':
    app.run(debug=True)