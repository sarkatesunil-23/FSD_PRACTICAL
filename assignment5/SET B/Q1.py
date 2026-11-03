from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST' ])
def employee():
    name =""
    department =""
    salary = ""

    if request.method == 'POST':
        name = request. form['name' ]
        department = request. form[ 'department' ]
        salary = request. form[ 'salary' ]

    return render_template('Q1.html',
                           name=name,
                           department=department,
                           salary=salary)

app.run(debug=True)