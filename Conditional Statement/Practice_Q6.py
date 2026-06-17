a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))

if a > b and a > c:
    print("Largest no is: ",a)
elif b > a and b > c:
    print("Largest no is: ",b)
else:
    print("Largest no is: ",c)
