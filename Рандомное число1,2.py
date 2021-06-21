Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:13:28) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
# Блок 1. Задача 2. Строки
randomString = input("введите строку - ")
print("Длина строки - ", len(randomString), "символа(ов)")
for i in randomString:
    if i == "c" or i == "C" or i == "с" or i == "С": # латиница и кириллица
        print("Символ <c> обнаружен")
print("Без 3-го символа-", randomString[0:2]+randomString[3:len(randomString)])
print("Без последнего символа-", randomString[:len(randomString)-1])