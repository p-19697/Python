from flask import Flask,render_template

app = Flask(__name__)

# Student Records
stud = [
    {"name": "Pranjali", "roll": 1, "marks": 96},
   {"name": "Aarti", "roll": 2, "marks": 90},
   {"name": "Dhanasree", "roll": 3, "marks": 89},
   {"name": "Poonam1", "roll": 4, "marks": 88},
]

# Route 1 - Homepage
@app.route('/')
def home():
    return render_template('home.html')
    
# Route 2 - Student Records
@app.route('/about')
def about():
      return render_template('about.html')

# Route 3 - Notice Board
@app.route('/student')
def student():
    return render_template('student.html', students=stud)

if __name__ == '__main__':
     print("INSIDE MAIN")
     app.run(debug=True)

