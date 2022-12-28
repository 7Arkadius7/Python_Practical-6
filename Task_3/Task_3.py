#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform

n =int(input('Пожалуйста, введите размер списка: '))

my_list = [round(uniform(0,11),2) for i in range(n)]
new_list = [round(i%1,2) for i in my_list]
print(f"Разницу между максимальным и минимальным значением дробной части чисел списка {my_list} равна {round(max(new_list) - min(new_list),2)}")