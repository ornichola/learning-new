"""
http://pythontutor.ru/lessons/dicts/problems/countries_and_cities/
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
"""

places = {}

for _ in range(int(input())):
    country, *cities = input().split()
    places[country] = cities

for _ in range(int(input())):
    city = input()
    for country in places:
        if city in places[country]:
            print(country)

"""
motherland = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        motherland[city] = country
        
for i in range(int(input())):
    print(motherland[input()])
"""
