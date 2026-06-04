from flask import Flask

app = Flask(__name__)

# Student Records
students = [
    {"name": "Pranjali", "course": "Computer Engineering", "year": "2nd Year"},
    {"name": "Aarti", "course": "Mechanical Engineering", "year": "3rd Year"},
    {"name": "Dhanashree", "course": "Civil Engineering", "year": "1st Year"},
    {"name": "Poonam", "course": "Electronics Engineering", "year": "2nd Year"}
]

# Route 1 - Homepage
@app.route('/')
def home():
    return """
    <h1>College Smart Portal</h1>
    <p>Welcome to the College Smart Portal.</p>
    <p>This portal provides student information, courses, and notices.</p>
    """

# Route 2 - Student Records
@app.route('/records')
def records():
    html = "<h1>Student Records</h1><ul>"

    for student in students:
        html += f""" <li>  Name: {student['name']} | Course: {student['course']} | Year: {student['year']} </li>
        """

    html += "</ul>"
    return html

# Route 3 - Notice Board
@app.route('/notice')
def notice():
    return """
    <h1>Notice Board</h1>
    <p>Semester Examination will start from 15 June 2026.</p>
    <p>Project submission last date is 10 June 2026.</p>
    """

if __name__ == '__main__':
    app.run(debug=True)