# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input('Пожалуйста, ведите число: ')
summa = sum([int(i) for i in num if i.isdigit()])
print(summa)