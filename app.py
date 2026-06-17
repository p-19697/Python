from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'pranjali9325'



college = {
    "name": "Government Polytechnic Hingoli",
    "location": "Hingoli, Maharashtra",
    "established": 1985,
    "affiliation": "MSBTE",
    "departments": "Computer Engineering, Electronics Engineering, Mechanical Engineering",
    "courses": "CO, EJ, ME",
    "library_books": "15000+",
    "computer_labs": 4,
    "status": "Active"
}

students = [
    {"id": "CO101","name": "Pranjali Gursude","department": "Computer Engineering","year": "Second Year","attendance": "92%","cgpa": "8.7" },
    { "id": "EJ102", "name": "Sneha Shinde", "department": "Electronics Engineering", "year": "Third Year", "attendance": "89%", "cgpa": "8.4" },
    {"id": "ME103","name": "Priya Patil","department": "Mechanical Engineering","year": "First Year","attendance": "95%","cgpa": "8.9" },
    {"id": "CO103","name": "Aarti More","department": "Computer Engineering","year": "Second Year","attendance": "92%","cgpa": "8.7" },
    {"id": "EJ106","name": "Poonam Kurhe","department": "Electronics Engineering","year": "Third Year","attendance": "95%","cgpa": "8.8" },
    {"id": "ME110","name": "kaveri Wankhede","department": "Mecanical Engineering","year": "Second Year","attendance": "98%","cgpa": "8.6" },
    {"id": "CO112","name": "Dhanashree Pole","department": "Computer Engineering","year": "Third Year","attendance": "93%","cgpa": "8.3" },
    {"id": "EJ113","name": "Gaytri Hippale","department": "Electronics Engineering","year": "Second Year","attendance": "97%","cgpa": "8.4" },
    {"id": "CO111","name": "Mohini Ghuge","department": "Computer Engineering","year": "Third Year","attendance": "96%","cgpa": "8.1" },
    {"id": "ME234","name": "Vaishnavi Deshmukh","department": "Mechanical Engineering","year": "Second Year","attendance": "90%","cgpa": "8.6" },
    {"id": "EJ542","name": "Tanuja Pattewar","department": "Electronics Engineering","year": "Third Year","attendance": "95%","cgpa": "8.8" },
    {"id": "ME513","name": "Siddhi Patil","department": "Mechamical Engineering","year": "Second Year","attendance": "99%","cgpa": "8.4" },
    {"id": "CO258","name": "Srushti kadam","department": "Computer Engineering","year": "Third Year","attendance": "98%","cgpa": "8.5" },
    {"id": "EJ546","name": "Yogita Dalvi","department": "Electronic Engineering","year": "Second Year","attendance": "92%","cgpa": "8.6" },


]

notices = [
    "Semester Examination starts from 15 June 2026",
    "Scholarship Form Submission Last Date: 20 June 2026",
    "Campus Placement Drive on 25 June 2026",
    "Industrial Visit Registration Open",
    "Library Membership Renewal Notice",
    "Project Exhibition on 30 June 2026"
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/records")
def records():
    return render_template(
        "records.html",
        college=college,
        students=students
    )

@app.route("/notice")
def notice():
    return render_template(
        "notice.html",
        notices=notices
    )

@app.route("/about")
def about():
    return render_template(
        "about.html",
        college=college
    )


@app.route("/add", methods=["GET", "POST"])
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

        new_student = {
            "id": student_id,
            "name": name,
            "department": department,
            "year": year,
            "attendance": attendance,
            "cgpa": cgpa
        }

        students.append(new_student)

        # Success Flash Message
        flash(f"Student {name} added successfully!", "success")

        # Redirect After Submit
        return redirect(url_for("records"))
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)