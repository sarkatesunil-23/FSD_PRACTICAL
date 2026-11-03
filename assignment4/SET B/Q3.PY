from flask import Flask

app = Flask(__name__)

@app.route('/employee')
def employee():
    return "Employee Page"

@app.route('/department')
def department():
    return "Department Page"

@app.route('/contact')
def contact():
    return "Contact Page"

if __name__ == '__main__':
    app.run(debug=True)