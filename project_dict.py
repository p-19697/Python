#college smart portal
portal_info=[
    {
        "portal name":"College smart portal",
        "college name":"Government polytechnic,Hingoli",
        "location":"Hingoli",
        "college code": 12345,
        "Departments":"Computer,Electronics,Mechanical",
        "courses":"CO,EJ,ME",
        "status":"active",
    }
]

#list student record
students=[
    {
        "name":"Pranjali",
        "enrollment no": 1010,
        "Department":"Computer",
        "cource":"CO",
        "contact no": 9876543210,
    },
    {
        "name":"Aarti",
        "enrollment no": 1011,
        "Department":"Electronics",
        "cource":"EJ",
        "contact no": 8765402102,
    },
    {
        "name":"Pooja",
        "enrollment no": 1012,
        "Department":"Mechanical",
        "cource":"ME",
        "contact no": 7654321098,
    },
    {
        "name":"Rohit",
        "enrollment no": 1013,
        "Department":"Computer",
        "cource":"CO",
        "contact no": 6543210987,
    },
    {
        "name":"Ramesh",
        "enrollment no": 1014,
        "Department":"Electronics",
        "cource":"EJ",
        "contact no": 5432109876,
    },
]
#get satus() fun
def get_status():
    return portal_info[0]["status"]

#search student record using search_records()function

def search_student_records(student_name):
    for student in students:
        if student["name"].lower() == student_name.lower():
            print("Student record found")
            for key, value in student.items():
                print(key, ":", value)
            return
    print("Student record not found")

#second dictionary

teachers=[
   {
      "teacher name":"Mr. Sharma",
      "Department":"Computer",
      "subject":"java",
      "experience": "10 years",
      "salary": 50000
   },
   {
        "teacher name":"Ms. Singh",
        "Department":"Electronics",
        "subject":"BEE",
        "experience": "8 years",
        "salary": 40000
     },
     {
        "teacher name":"Mr. Verma",
        "Department":"Mechanical",
        "subject":"MEM",
        "experience": "7 years",
        "salary": 60000
   },
   {
        "teacher name":"Ms. Patel",
        "Department":"Computer",
        "subject":"python",
        "experience": "5 years",
        "salary": 45000
   },
   {
        "teacher name":"Mr. Kumar",
        "Department":"Electronics",
        "subject":"EDC",
        "experience": "6 years",
        "salary": 55000
   }
]

def search_teacher_record(teacher_name):
    for teacher in teachers:
       if teacher["teacher name"].lower() == teacher_name.lower():
            print("Teacher record found")
            for key, value in teacher.items():
                print(key, ":", value)
            return
    print("Teacher record not found")

print("***** COLLEGE PORTAL INFORMATION *****")
for info in portal_info:
    for key, value in info.items():
        print(key, ":", value)

print("\nCollege Portal Status :", get_status())

print("\n****STUDENT RECORDS****")
name = input("Enter Student Name: ")
search_student_records(name)

print("****TEACHER RECORDS****")
tname = input("Enter Teacher Name: ")
search_teacher_record(tname)
