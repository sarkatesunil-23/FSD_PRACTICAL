from flask import Flask
import psycopg2

app = Flask(__name__)
def db_connect():

    conn = psycopg2.connect(
        dbname = "hospital",
        user = "postgres",
        password ="root",
        host = "localhost",
        port = "5432"
    )
    return conn

    
@app.route('/create_table')
def create_table():

    try:

            conn = db_connect()
            cur = conn.cursor()
         
            cur.execute("""
                 CREATE TABLE IF NOT EXISTS patient (
                     id SERIAL PRIMARY KEY,
                     name VARCHAR(50),
                     age INT,
                     disease VARCHAR(50)
                 );

       """)

            conn.commit()
            cur.close()
            conn.close()

            return "patient table created succesfully"

    except Exception as e:
         return f"Error :(e)"

    @app.route('\insert')
    def insert_record():

         conn = db_connect()
         cur = conn.cursor()

         patients=[
              ("alice",30,"flu"),
              ("bob",25,"migrane")
         ]

        cur.executemany(
             "insert into patient (name,age,disease"
        )



if __name__=='__main__':
    app.run(debug=True)