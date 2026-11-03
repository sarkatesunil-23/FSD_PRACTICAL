from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('feedback.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    name = request.form['name']
    message = request.form['message']

    return f"Thank you {name}! Your feedback: {message}"

if __name__ == '__main__':
    app.run(debug=True)