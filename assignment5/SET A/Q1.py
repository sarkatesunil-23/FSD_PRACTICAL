from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST' ])
def student():
    name = ""

    if request.method == 'POST':
       name = request.form['name' ]

    return render_template('Q1.html', name=name)

app.run(debug=True)