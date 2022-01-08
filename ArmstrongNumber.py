'''
@Author: Hitesh Patil
@Date: 08-01-2022 10:05:46
@Last Modified by: Hitesh Patil
@Last Modified time: 08-01-2022 11:05:00
@Title : Program For Finding Armstrong Number
'''

user_num = int(input("Enter a Integer Number: "))

result=0

num=user_num
while num > 0:
    reminder= num % 10
    result=result+(reminder**3)
    num //=10


if result==user_num:
    print ("\n", user_num, "This number is an Amstrong Number\n")
else:
    print("\n", user_num, "This number is not an Amstrong Number\n")
    
exit