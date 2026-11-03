from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    name = request.form['name']
    return "Search Result: Student Name is " + name

if __name__ == '__main__':
    app.run(debug=True)