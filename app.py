from flask import Flask, render_template

app = Flask(__name__)

students = [
    {"department": "Computer", "enrollment": 24510290065, "name": "Pranjali", "roll": 101},
    {"department": "Electronics", "enrollment": 24510290066, "name": "Aarti", "roll": 102},
    {"department": "Mechanical", "enrollment": 24510290067, "name": "Dhanashree", "roll": 103},
    {"department": "Electronics", "enrollment": 24510290068, "name": "Poonam", "roll": 104},
    {"department": "Computer", "enrollment": 24510290069, "name": "Kaveri", "roll": 105},

]

notices = [
    "1st Unit Test starts from 15 June 2026",
    "2nd Unit Test starts from 6 Augst 2026",
    "Project Submission Date: 20 June 2026",
    "College Annual Function on 25 June 2026",
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/records')
def records():
    return render_template('records.html', students=students)

@app.route('/notice')
def notice():
    return render_template('notice.html', notices=notices)

if __name__ == "__main__":
    app.run(debug=True)