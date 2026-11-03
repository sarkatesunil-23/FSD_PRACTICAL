from flask import Flask, request, jsonify

app = Flask(__name__)

employee = {
    "name": "XYZ",
    "department": "IT"
}

@app.route('/employee', methods=['GET'])
def get_employee():
    return jsonify(employee)

@app.route('/addemployee', methods=['POST'])
def add_employee():
    data = request.get_json()

    return jsonify({
        "employee": data,
        "msg": "Employee added successfully"
    })

if __name__ == '__main__':
    app.run(debug=True)