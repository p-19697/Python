students =["dipak","kartik","satyarth","satyarth","satyarth"]
print(students)
print (students[0])
print (students[1])
print (students[2])
print (students[3])
print (students[4])

#Loop -TO print all the elements in the list
for student in students:
    print(f"hello {student} Welcome to the class")  


marks=[98,99,95,90]
for i in marks:
    if i>=90:
        print(f"Excellent! You got {i} marks")

    elif i>=60:
        print(f"Good! You got {i} marks")
    elif i>=40:
        print(f"you are passed with {i} marks")
    else:
        print(f"you are failed with {i} marks")

for i in range(1,6):
    print(i)

'''function it is a block of code which we write only once and whnever we need it
we can call it multipke times'''

def greet(name):
    print(f"Hello {name} Welcome to the class")

for student_name in students:
    greet(student_name)