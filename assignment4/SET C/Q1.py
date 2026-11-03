from flask import Flask

app = Flask(__name__)

@app.route('/product/<int:id>')
def product(id):
 return "Product ID: " + str(id) + "<br>Product Details:Computer Product"

if __name__ == '__main__':
    app.run(debug=True)