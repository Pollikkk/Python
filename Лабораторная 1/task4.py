users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
visits = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

kol = len(users)
uniq_kol = len(set(users))

visits["Общее количество"] = kol
visits["Уникальные посещения"] = uniq_kol

print(visits)