from flask import Flask
import psycopg2

app = Flask(__name__)
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="company1",
        user="postgres",
        password="root",
        port="5432"
    )
@app.route('/createtable')
def createtable():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            emp_id INTEGER PRIMARY KEY,
            name VARCHAR(50),
            department VARCHAR(50),
            salary NUMERIC(10,2)
        )
    """)

    conn.commit()
    cur.close()
    conn.close()

    return "Employee Table Created Successfully!"

@app.route('/insertreco')
def insertreco():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO employee (emp_id, name, department, salary)
        VALUES
        (1, 'Priya', 'IT', 30000),
        (2, 'Rahul', 'HR', 25000),
        (3, 'Amit', 'Finance', 35000)
        ON CONFLICT (emp_id) DO NOTHING
    """)

    conn.commit()
    cur.close()
    conn.close()

    return "Employee Records Inserted Successfully!"

@app.route('/getdetails/<int:emp_id>')
def getdetails(emp_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT name, department, salary FROM employee WHERE emp_id = %s",
        (emp_id,)
    )

    employee = cur.fetchone()

    cur.close()
    conn.close()

    if employee:
        return {
            "Employee ID": emp_id,
            "Name": employee[0],
            "Department": employee[1],
            "Salary": float(employee[2])
        }

    return {"message": "Employee Not Found"}
if __name__ == '__main__':
    app.run(debug=True)

