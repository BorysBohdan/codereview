"""
Вивести кількість слів, що починаються з великої літери.
"""



text=input("Введіть текст :\n")
List=text.split()
print("Слова, що починаються з великої літери : ")
for word in List:
    letter=list(word)
    Firsl_letter=str.upper(letter[0])
    if Firsl_letter==str(letter[0]):
        print(str(word))