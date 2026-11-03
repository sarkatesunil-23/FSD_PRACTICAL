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
        CREATE TABLE IF NOT EXISTS employee1 (
            emp_id INTEGER PRIMARY KEY,
            name VARCHAR(50),
            department VARCHAR(50),
            salary NUMERIC(10,2)
        )
    """)

    conn.commit()
    cur.close()
    conn.close()

    return "Employee1 Table Created Successfully!"
@app.route('/insertreco')
def insertreco():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO employee1 (emp_id, name, department, salary)
        VALUES
        (1, 'Priya', 'IT', 30000),
        (2, 'Rahul', 'HR', 25000),
        (3, 'Amit', 'Finance', 35000),
        (4, 'Pranita', 'Marketing', 28000),
        (5, 'Rohan', 'Sales', 32000)
        ON CONFLICT (emp_id) DO NOTHING
    """)

    conn.commit()
    cur.close()
    conn.close()

    return "5 Employee Records Inserted Successfully!"

@app.route('/update_salary/<int:emp_id>/<int:salary>')
def updatesalary(emp_id, salary):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE employee1 SET salary = %s WHERE emp_id = %s",
        (salary, emp_id)
    )

    updated = cur.rowcount

    conn.commit()
    cur.close()
    conn.close()

    if updated > 0:
        return f"Salary Updated Successfully for Employee ID {emp_id}!"
    else:
        return "Employee1 Not Found!"
    
@app.route('/delete_employee1/<int:emp_id>')
def deleteemployee(emp_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM employee1 WHERE emp_id = %s",
        (emp_id,)
    )

    deleted = cur.rowcount

    conn.commit()
    cur.close()
    conn.close()

    if deleted > 0:
        return f"Employee ID {emp_id} Deleted Successfully!"
    else:
        return "Employee Not Found!"

@app.route('/finalrecords')
def finalrecords():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT emp_id, name, department, salary FROM employee1 ORDER BY emp_id"
    )

    employees = cur.fetchall()

    cur.close()
    conn.close()

    result = "<h2>Final Employee Records</h2>"

    if not employees:
        return "No Employee Records Found!"

    result += """
        <table border="1" cellpadding="8">
        <tr>
            <th>Employee ID</th>
            <th>Name</th>
            <th>Department</th>
            <th>Salary</th>
        </tr>
    """

    for emp in employees:
        result += f"""
        <tr>
            <td>{emp[0]}</td>
            <td>{emp[1]}</td>
            <td>{emp[2]}</td>
            <td>{emp[3]}</td>
        </tr>
        """

    result += "</table>"

    return result


if __name__ == '__main__':
    app.run(debug=True)

