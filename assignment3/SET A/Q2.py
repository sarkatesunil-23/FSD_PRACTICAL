from flask import Flask

app = Flask(__name__)

@app.route('/')
def student():
    return "Name: Pranita Bhagwat<br>Roll No: 13"

if __name__ == '__main__':
    app.run(debug=True)