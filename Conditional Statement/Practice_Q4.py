sub1 = int(input("Enter marks of sub1: "))
sub2 = int(input("Enter marks of sub2: "))
sub3 = int(input("Enter marks of sub3: "))
sub4 = int(input("Enter marks of sub4: "))
sub5 = int(input("Enter marks of sub5: "))

tot = sub1 + sub2 + sub3 + sub4 + sub5
per = (tot/500)*100
print("Percentage of sub marks: ", per)
print("\n")
if per >= 75:
    print("Honours")
elif (per>=60 and per<75):
    print("First Division")
elif (per>=45 and per<60):
    print("Second Division")
elif (per>=35 and per<45):
    print("Third Division")
else:
    print("Fail")