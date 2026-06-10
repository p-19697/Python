from flask import Flask, render_template

app = Flask(__name__)

students = [
    {   "id": 1, "name": "Pranjali Gursude", "department": "Computer Engineering","attendance": "92%", "marks": 88 },
    {  "id": 2, "name": "Aarti More", "department": "Mechanical Engineering", "attendance": "85%", "marks": 80 },
    {  "id": 3,  "name": "Dhanashree Pole", "department": "Electronics Engineering","attendance": "90%", "marks": 91},
    {"id": 4,"name": "Poonam Kurhe","department": "Computer Engineering","attendance": "98%","marks": 99 },
    {"id": 5,"name": "Gauri Deshmukh","department": "Electronics Engineering","attendance": "90%","marks": 95},
    {"id": 6,"name": "kaveri Wankhede","department": "Mechanical Engineering","attendance": "99%","marks": 99},
    {"id": 7,"name": "Vaibhavi patil","department": "Computer Engineering","attendance": "90%","marks": 91}
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/records")
def records():
    return render_template("records.html", students=students)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/record/<int:id>")
def record(id): 
    student = None

    for s in students:
        if s["id"] == id:
            student = s
            break

    return render_template("record_detail.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)