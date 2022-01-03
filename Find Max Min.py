print ("Enter Any Three Numbers")

a = float (input("Enter 1st no:  "))
b= float (input ("Enter 2nd no:  "))
c= float  (input ("Enter 3rd no:  "))

print ("Highest Number is:", end='')

if (a>b) and (a>c):
    print (a)
elif (b>a) and  (b>c):
    print(b)
else:
    print (c)


print ("Lowest Number is:", end='')
if (a<b) and (a<c):
    print (a)
elif (b<a) and  (b<c):
    print(b)
else:
    print (c)

exit





