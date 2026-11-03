from flask import Flask

app = Flask(__name__)

@app.route('/')
def department():
    return "Welcome to the B.Sc. IT Department of Samarth College of Computer Science."

if __name__ == '__main__':
    app.run(debug=True)