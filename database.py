import sqlite3
from flask import Flask, render_template, request, flash
app=Flask(__name__)
app.secret_key="pranjali008"

#2 functions
def get_db():
    """Database connection"""
    conn=sqlite3.connect('college.db')
    conn.row_factory = sqlite3.Row #to access coloumn by name
    return conn

def init_db():
    """Create table"""
    conn = get_db()
    #Create Student table if it doesn't exist
    conn.execute('''
                 CREATE TABLE IF NOT EXISTS students (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 department TEXT NOT NULL,
                 year TEXT NOT NULL,
                 attendance INTEGER DEFAULT 0,
                 cgpa REAL NOT NULL
                 )
                   ''' )
    conn.commit()
    conn.close()

if __name__=="__main__":
    init_db() #Initialize database
    app.run(debug=True)
    print("Database created successfully!")