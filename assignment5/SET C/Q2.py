from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def order():

    if request.method == 'POST':
        product = request.form['product']
        quantity = request.form['quantity']
        price = request.form['price']

        return "Product Name: " + product + "<br>" + \
               "Quantity: " + quantity + "<br>" + \
               "Price: " + price

    return render_template('q2.html')


if __name__ == '__main__':
    app.run(debug=True)