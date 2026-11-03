from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product', methods=['POST'])
def product():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = num1 * num2
    return f"Product = {result}"

if __name__ == '__main__':
    app.run(debug=True)