
from store.models import Wear


def create_wear_obj_answer(obj: Wear):
    obj_msg = (f"""Товар: {obj.name}
Размер: {obj.size}
Цвет: {obj.color}
Материал: {obj.material}
Пол: {obj.sex}
Цвет: {obj.age}
Марка: {obj.brand}
Цена: {obj.price}
Описание: {obj.description}
""")

    return obj_msg
# \n
