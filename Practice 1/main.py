from fastapi import FastAPI
import json
from models import *

app = FastAPI()


@app.get("/")
def main():
    return "Hello world"


@app.get('/warriors/')
def list_warriors():
    return temp_bd


@app.get("/warriors/{id}")
def get_warrior(id: int):
    return [warrior for warrior in temp_bd if warrior['id'] == id]


@app.post('/warrior/')
def create_warrior(warrior: Warrior):
    temp_bd.append(warrior)
    return {"status": 200, "data": warrior}


@app.delete("/warrior/{id}")
def delete_warrior(id: int):
    for i, warrior in enumerate(temp_bd):
        if warrior.get("id") == id:
            temp_bd.pop(i)
            break
    return {"status": 200, "data": "warrior is deleted"}


@app.put("/warrior/{id}")
def update_warrior(new_warrior: Warrior, id: int):
    for i in range(len(temp_bd)):
        if temp_bd[i]['id'] == id:
            temp_bd[i] = new_warrior
            return {"status": 400, "data": "warrior is modified"}


temp_bd = [
    {
        "id": 1,
        "race": "director",
        "name": "Мартынов Дмитрий",
        "level": 12,
        "profession": {
            "id": 1,
            "title": "Влиятельный человек",
            "description": "Эксперт по всем вопросам"
        },
        "skills":
        [{
            "id": 1,
            "name": "Купле-продажа компрессоров",
            "description": ""

        },
            {
            "id": 2,
            "name": "Оценка имущества",
            "description": ""

        }]
    },
    {
        "id": 2,
        "race": "worker",
        "name": "Андрей Косякин",
        "level": 12,
        "profession": {
            "id": 1,
            "title": "Дельфист-гребец",
            "description": "Уважаемый сотрудник"
        },
        "skills": []
    },
]
