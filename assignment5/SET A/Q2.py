from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST' ])
def addition():
    a = ""
    b = ""
    result = ""

    if request.method == 'POST':
        a = request. form['a']
        b = request.form['b']
        result = int(a) + int(b)

    return render_template('Q2.html', a=a, b=b, result=result)

app.run(debug=True)