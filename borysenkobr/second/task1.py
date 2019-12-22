"""
    Використовуючи регулярні вирази, для поданого тексту зробіть аби
    усі речення починалися з великої букви. Виведіть результат.
                                                                """

import re

pattern = re.compile("^(\w+(\W+)*.\s*)+$")

def validator(pattern,promt):
    text=input(promt)
    while not bool(re.match(pattern,text)):
        text = input(promt)
    print(text)
    return text

def swap(text):
    text=re.split(r'[.]*\s', text)
    print(text)
    for element in text:
        pass
    return text
print(swap(validator(pattern,"Введіть текст: ")))
