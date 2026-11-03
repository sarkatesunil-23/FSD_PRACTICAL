from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route('/')
def birthday():
    today = date.today()
    return "Happy Birthday Dear!! 🎂<br>Today's Date: " + str(today)

if __name__ == '__main__':
    app.run(debug=True)