import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app=Flask(__name__)
app.secret_key='pranjali008'

def get_db():
    conn = sqlite3.connect('practice.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS students(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 department TEXT NOT NULL,
                 year TEXT NOT NULL,
                 attendance INTEGER DEFAULT 0,
                 cgpa REAL NOT NULL
                 )''')
    conn.commit()
    conn.close()

    @app.route('/')
    def home():
        conn=get_db()
        students=conn.execute('SELECT * FROM students ORDER BY id DESC').fetchall
        conn.close()
        return render_template('home.html',students=students)
    
    def add():

     if request.method == "POST":

        student_id = request.form.get("id")
        name = request.form.get("name")
        department = request.form.get("department")
        year = request.form.get("year")
        attendance = request.form.get("attendance")
        cgpa = request.form.get("cgpa")

        # Validation - Empty Check
        if not student_id or not name or not department or not year or not attendance or not cgpa:
            flash("All fields are required!", "danger")
            return redirect(url_for("add"))
        
        conn =  get_db()

        conn.execute(''' INSERT INTO students
                     (name, department, year, attendance, cgpa)VALUES (?, ?, ?, ?, ?)''',
                     (name,department,year,int(attendance),float(cgpa))
                    )
        

        conn.commit()
        conn.close()

        # Success Flash Message
        flash(f"Student {name} added successfully!", "success")
       
        # Redirect After Submit
        return redirect(url_for("records"))
    return render_template("add.html")

@app.route('/delete/<init:id>')
def delete_student(id):
   conn = get_db()

   student = conn.execute('DELETE FROM students WHERE id = ?',(id))
   conn.commit()
   conn.close()

   flash(f"{student['name']}deleted successfully",'success')
   return redirect(url_for('records'))