from flask import Flask, render_template
import flask

app= Flask(__name__)

#project data - dictionary dynamic

studentss=[
    {"name":"Rahul","marks":95,"Roll no":1},
    {"name":"Satyarth","marks":85,"Roll no":2},
    {"name":"Pratik","marks":75,"Roll no":3},
    {"name":"Kartik","marks":65,"Roll no":4},

]

@app.route('/')
def home():
    #Creat using HTml
    return  render_template ("home.html")


    return '<h1>Colage Portal</h1>'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Students')
def Students():
    return render_template('Students.html', students=studentss)
if __name__=="__main__":
    app.run(debug=True)