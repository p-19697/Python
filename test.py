#virtual environment

#1 create a virtual environment
# python -m venv.myenv
#2 activate the virtual environment
#for window : .\myenv\Scripts\activate

#after activating the virtual enviornment 
#pip.list

#Dictionary - key value pair

student={
    "name":"Rahul",
    "roll no": 101,
    "marks":95,
    "subjects":"java"
}

#accessing values from Dictionary

print(student["name"])
print(student["roll no"])
print(student["marks"])
print(student["subjects"])

#update values in dictionary

student["marks"]=100
print(student["marks"])

#Adding a new field

student["grade"]="A"
print(student["grade"])

#check field available or not

print("name"in student)
print("age"in student)

#checling how many keys or values in dictionary

print(student.keys())
print(student.values())

#Collage portal

student=[
    {
        "name": "Rahul",
        "roll no":101,
        "marks": 95,
        "subjects": "java"
    },
    {
        "name": "Rohit",
        "roll no": 102,
        "marks": 90,
        "subjects": "python"
    },
    {
        "name": "Ramesh",
        "roll no": 103,
        "marks": 85,
        "subjects": "c++"
    },
    {
        "name": "Suresh",
        "roll no": 104,
        "marks": 80,
        "subjects": "javascript"
    },
    {
        "name": "Mahesh",
        "roll no": 105,
        "marks": 75,
        "subjects": "html"

    },
]


#Accesing student informtion 

print(student[0])
print(student[0]["name"])
print(student[1]["marks"])

#loop 

for students in student:
    print(f"{students['name']} scored {students['marks']} in subject {students['subjects']}")