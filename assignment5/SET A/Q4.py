from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def result():

    if request.method == 'POST':
        marks = int(request.form['marks'])

        if marks >= 40:
            result = "Pass"
        else:
            result = "Fail"

        return "Result: " + result

    return render_template('q4.html')

if __name__ == '__main__':
    app.run(debug=True)