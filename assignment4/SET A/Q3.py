from flask import Flask

app = Flask(__name__)

@app.route('/course/<name>')
def course(name):
    return "Course Name: " + name + "<br>Course Information: This is a computer course."

if __name__ == '__main__':
    app.run(debug=True)