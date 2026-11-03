from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def date_time():
    now = datetime.now()
    return "Current Date and Time: " + str(now)

if __name__ == '__main__':
    app.run(debug=True)