# страны и их аббревиатуры
states = {
    'Россия': 'RU',
    'Германия': 'DE',
    'Узбекистан': 'UZ',
    'Зимбабве': 'ZW',
    'Турция': 'TR'
}

# город страны
cities = {
    'UZ': 'Газли',
    'TR': 'Сарыгерме',
    'DE': 'Мюнхен'
}

# добавляем города
cities['ZW'] = 'Гверу'
cities['RU'] = 'Москва'

# выводим города нескольких стран
print('-' * 10)
print("в ZW есть город", cities['ZW'])
print("в RU есть город", cities['RU'])

# вывод нескольких стран
print('-' * 10)
print("Аббревиатура Турции:", states['Турция'])
print("аббревиатура Германии: ", states['Германия'])

# выводим города других нескольких стран
print('-' * 10)
print("В Турции есть город", cities[states['Турция']])
print("В Германии есть город", cities[states['Германия']])

# все аббревиатуры
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} имеет аббревиатуру {abbrev}")

# все города
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"В стране {abbrev} есть город {city}")

# 2 типа данных
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"B стране {state} используется аббревиатура {abbrev}")
    print(f"и есть город {cities[abbrev]}")

print('-' * 10)
# безопасное получение аббревиатуры страны, которая не представлена
state = states.get('usa')

