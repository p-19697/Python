from flask import Flask
import flask

app= Flask(__name__)

#project dada - dictionary dynamic

stud=[
    {"name":"Rahul","marks":95,"Roll no":1},
    {"name":"Satyarth","marks":85,"Roll no":2},
    {"name":"Pratik","marks":75,"Roll no":3},
    {"name":"Kartik","marks":65,"Roll no":4},

]

@app.route('/')

def home():
    #Creat using HTml
    

    return '<h1>Colage Portal</h1>'

@app.route('/about')
def about():
    return '<h1>About Us</h1><p>This is Collage management system.</p>'

@app.route('/Students')
def Students():
    return '<h1>Students list</h1><p>Student will show here.</p>'

if __name__=="__main__":
    app.run(debug=True)