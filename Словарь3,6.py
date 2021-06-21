Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:13:28) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Блок 3. Задача 6. Словарь
list1 = input("Введите первый список через запятую: ")
list1 = list1.split(",")
# множество (?)
arrayList1=set(list1)
#print(arrayList1)
countWordList1 = len(list1)
print("В списке {} слов(а)".format(countWordList1))
list2 = input("Введите второй список из {} слов через запятую: ".format(countWordList1))
list2 = list2.split(",")
dictionaryList = dict(zip(list1, list2))
print(dictionaryList)