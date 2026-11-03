from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def check_login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password =='1234':
        return "Login Successful"
    else:
        return "Invalid Username or Password"

if __name__ == '__main__':
    app.run(debug=True)