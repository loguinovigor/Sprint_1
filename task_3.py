world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

# Добавляем 2022 год
world_champions[2022] = 'Аргентина'

# Выводим чемпионов
for year, country_name in world_champions.items():
    print(f'{year} - {country_name}')

# Проверяем, выигрывала ли Италия
country = 'Италия'

if country in world_champions.values():
    print('Италия становилась чемпионом мира по футболу в 21 веке!')
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')
