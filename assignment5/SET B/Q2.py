from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def feedback():

    if request.method == 'POST':
        name = request.form['name']
        rating = request.form['rating']
        comments = request.form['comments']

        return "Name: " + name + "<br>" + \
               "Rating: " + rating + "<br>" + \
               "Comments: " + comments

    return render_template('q2.html')

if __name__ == '__main__':
    app.run(debug=True)