from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('library.html')

@app.route('/search', methods=['POST'])
def search():
    book = request.form['book']

    if book == "Python":
        return "Book Found: Python"
    else:
        return "Book Not Found"

if __name__ == '__main__':
    app.run(debug=True)