from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('student.html')

@app.route('/student', methods=['POST'])
def student():
    name = request.form['name']
    return "Student Name: " + name

if __name__ == '__main__':
    app.run(debug=True)