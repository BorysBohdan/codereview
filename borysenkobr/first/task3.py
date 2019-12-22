"""
Виведення сум парних та непарних чисел у списку.
"""

List=[1,2,5,7,3,9,2,10,15,4]
parni=0
ne_parni=0
for x in List:
    if x%2 :
        parni+=x
    else:
        ne_parni+=x
print("Сумою парних чисел є число " + str(parni))
print("Сумою непарних чисел є число " + str(ne_parni))
