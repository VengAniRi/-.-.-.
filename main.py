# DZ_1
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

russia_countries = []
for obj in geo_logs:
    countries = list(obj.values())[0]
    if 'Россия' in countries:
        russia_countries.append(countries)

print(*russia_countries, sep='\n')
print('---------')

# DZ_2

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


ids_set = set()
for id_list in ids.values():
    ids_set |= set(id_list)

print(list(ids_set))
print('---------')

# DZ_3

queries = [
    'смотреть сериалы онлайн',
    'смотреть фильмы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'Python',
    'programming'
    ]

stats_queries = {}
for query in queries:
    words_count = len(query.split())
    if words_count not in stats_queries: # запроса с таким кол-вом слов не было в словаре
        stats_queries[words_count] = 1
    else: # встретили запрос с тем кол-вом слов, которое уже встречали
        stats_queries[words_count] += 1


for words_count, queries_count in stats_queries.items():
    print(f"Кол-во поисковых запросов из {words_count} слов(-а): {queries_count / len(queries) * 100 : .2f}%")
print('---------')

# DZ_4

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
print("Канал с максимальным объемом:", max(stats.items(), key=lambda t: t[1]) [0])