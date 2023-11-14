# TODO решите задачу
import json

def task() -> float:
    sum = 0
    # Чтение данных из файла в формате JSON
    with open('input.json') as file:
        data = json.load(file)
        for line in data:
            sum += line["score"] * line["weight"]
    return(round(sum, 3))


print(task())
