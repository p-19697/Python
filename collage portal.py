#collage smart portal project
#Student details
student=["Pranjali","Aarti","Dhanashree","Pavan"]
roll_no=[101,102,103,104]
marks=[98,99,95,90]
attendence=[68,70,75,80]

notice=[ "Semester Exam starts from 15 June",
    "Submit assignment before 10 June",
    "College fest on 20 June"
    ]

def student_login():
    name=input("Enter student name :")
    rollno=int(input("Enter student roll number :"))
    for i in range(len(student)):

        if student[i]==name and roll_no[i]==rollno:
            print("Login successfully")
            print ("Welcome to the student portal")
            print("***Student Details***")
            print("Name:",name)
            print("Roll No:",roll_no[i])
            print("Marks:",marks[i])
            print("Attendence:",attendence[i])
            print("Notice Board")
            print(notice)
            print("Thank you for using the student portal")
        
            return 
        else :
             print("login unsuccesssfully")
             
student_login()    