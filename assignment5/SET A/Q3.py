from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rectangle():

    if request.method == 'POST':
        length = float(request.form['length'])
        breadth = float(request.form['breadth'])

        area = length * breadth

        return "Area of Rectangle = " + str(area)

    return render_template('q3.html')

if __name__ == '__main__':
    app.run(debug=True)