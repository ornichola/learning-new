"""
[STEPIK]
Python: основы и применение https://stepik.org/512
03_04_01 Распространённые форматы текстовых файлов: CSV, JSON
"""

"""
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года 
по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
"""

import csv
import time


YEAR = 2015

crimes_in_2015 = list()
with open('03_04_01.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if time.strptime(row.get('Date'), '%m/%d/%Y %I:%M:%S %p').tm_year == YEAR:
            crimes_in_2015.append(row)

crimes_by_type = dict()
for crime in crimes_in_2015:
    crime_type = crime.get('Primary Type')
    if not crimes_by_type.get(crime_type):
        crimes_by_type[crime_type] = list()
    crimes_by_type[crime_type].append(crime)

counted_crime_types = dict()
for crime_type in crimes_by_type:
    counted_crime_types[crime_type] = len(crimes_by_type[crime_type])

print(f'Most common crime in Chicago in year {YEAR}:')
print(max(counted_crime_types, key=counted_crime_types.get))
