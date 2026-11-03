from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)
def db_connect():
    return psycopg2.connect(
        dbname="company1",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )

def create_table():
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Employee2 (
            Employee_ID INT PRIMARY KEY,
            Name VARCHAR(100),
            Department VARCHAR(100)
        )
    """)

    con.commit()
    cur.close()
    con.close()
@app.route("/", methods=["GET", "POST"])
def employee():
    msg = ""
    emp = None

    if request.method == "POST":
        eid = request.form["Employee_ID"].strip()
        name = request.form["Name"].strip()
        department = request.form["Department"].strip()

        if eid == "" or name == "" or department == "":
            msg = "Please fill in all fields."

        else:
            con = db_connect()
            cur = con.cursor()

            cur.execute(
                """INSERT INTO Employee2
                (Employee_ID, Name, Department)
                VALUES (%s, %s, %s)""",
                (eid, name, department)
            )

            con.commit()

            emp = (eid, name, department)
            msg = "Employee information saved successfully!"

            cur.close()
            con.close()

    return render_template("employee.html", msg=msg, emp=emp)


if __name__ == "__main__":
    create_table()
    app.run(debug=True)