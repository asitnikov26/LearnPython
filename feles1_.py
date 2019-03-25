'''
Создайте список словарей:
        [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
Запишите содержимое списка словарей в файл в формате csv
'''

import csv
spisok = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    fiel = ['name', 'age', 'job']
    writ = csv.DictWriter(f, fiel, delimiter=';')
    writ.writeheader()
    for sp in spisok:
        writ.writerow(sp)
