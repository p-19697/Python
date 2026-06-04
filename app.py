from flask import Flask

app= Flask (__name__)

#project data - dynamic data insert 
stud=[
    {"name":"Dipak","roll no":101,"marks":98},
    {"name":"Aarti","roll no":102,"marks":99},
    {"name":"Pranjali","roll no":103,"marks":97},
    {"name":"Rohit","roll no":104,"marks":93},
]

@app.route('/')
def home():
    html = '<h1>College Smart Portal - Students</h1>'
    html += '<ul>'

    for student in stud:
        html += f"<li>{student['name']} - Roll No: {student['roll no']} - Marks: {student['marks']}</li>"

    html += '</ul>'
    return html 

@app.route('/about')
def about():
    return '<h1>About college smart portal<h1><p>This is college management system</p>'

@app.route('/student')
def student():
    return '<h1> student list<h1> <p> All students will be shown here</p>'


if __name__ == '__main__':
   app.run(debug=True)