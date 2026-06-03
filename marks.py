sub1 = int(input("Enter sub 1 maarks:"))
sub2 = int(input("Enter sub 2 maarks:"))
sub3 = int(input("Enter sub 3 maarks:"))
sub4 = int(input("Enter sub 4 maarks:"))
sub5 = int(input("Enter sub 5 maarks:"))

total= sub1 + sub2 + sub3 + sub4 + sub5 
percentage = total/5

print("Total marks :",total)
print("Percenntage :",percentage)


if percentage >= 70:
            print("Result = Distinction")

elif percentage >= 60:
            print("Result = first class")
elif percentage >= 45:
            print("Result = pass")
else:
            print("Result = Fail")
            print("Better luck next time")
            

