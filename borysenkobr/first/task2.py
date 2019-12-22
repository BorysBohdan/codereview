"""
Вивести кількість порожніх списків у списку.
"""


List=[[],1,2,3,[]]
Checking_list=[]
number=0
for x in List:
    if x == Checking_list:
        number+=1
print("У цьому списку " + str(number) + " порожніх списків" )