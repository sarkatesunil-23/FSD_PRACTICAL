from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def salary():

    if request.method == 'POST':
        basic = float(request.form['basic'])

        allowance = 2000
        total = basic + allowance

        return "Basic Salary: " + str(basic) + "<br>" + \
               "Fixed Allowance: " + str(allowance) + "<br>" + \
               "Total Salary: " + str(total)

    return render_template('q3.html')

if __name__ == '__main__':
    app.run(debug=True)