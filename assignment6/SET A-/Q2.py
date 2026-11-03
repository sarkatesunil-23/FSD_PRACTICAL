from flask import Flask

app = Flask(__name__)

@app.route("/")
def student_list():

    students = ["Om", "Rahul", "mehek", "sonu", "Sunil"]

    student_names = "<br>".join(students)
    
    return f"""
    <h2>List of Students</h2>
    {student_names}
    """

if __name__ == "__main__":
    app.run(debug=True)