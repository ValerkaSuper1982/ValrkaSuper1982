Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:13:28) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
# Блок 1. Задача 1. Сравнить числа
print("Введите число = ")
number = float(input())
print("Введите пограничное число = ")
numberP = float(input())
if number < numberP:
    print("Ваше число меньше пограничного")
elif number > numberP*3:
    print("Ваше число больше пограничного более, чем в 3 раза")
elif number > numberP:
    print("Ваше число больше пограничного")
else:
    print("Числа равны")