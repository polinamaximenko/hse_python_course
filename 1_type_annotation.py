"""
Аннотации типов
"""

from typing import List, Dict, Optional, Union, Any, Tuple


# Простые типы
name: str = "Анна"
age: int = 25
height: float = 1.75
is_active: bool = True


# Списки
names: List[str] = ["Анна", "Борис", "Виктор"]
scores: List[int] = [95, 87, 92]

# Словари
person: dict[str, any] = {"name": "Анна", "age": 25}
person_typed: Dict[str, Union[str, int]] = {"name": "Анна", "age": 25}
middle_name: Optional[str] = None  # может быть строкой или None
data: Any = {"что": "угодно"}

# Сложная структура
users: List[Dict[str, Union[str, int]]] = [
    {"name": "Анна", "age": 25},
    {"name": "Борис", "age": 30}
]

"""
Особенности:
- передают ошибку, если пользователь вводит иной тип данных
- поддерживаются IDE
- служат инструментом документации
- помогают снизить количество ошибок, 
  которые возникают из-за динамической типизации
- снижают количество try и except в коде
- может использоваться для улучшения безопасности кода
"""

def _extract_date(self, date_string: str) -> str:
    # Принимает строку, возвращает строку
    pass

def get_sample_posts(self, n: int = 5) -> List[Dict[str, Any]]:
    # Принимает int (по умолчанию 5), возвращает список словарей
    pass

def load_data(self, file_path: str) -> Dict[str, Any]:
    # Принимает строку, возвращает словарь
    pass

def process_user_data(
    self,
    user_id: int,
    include_metadata: bool = False
) -> Tuple[Dict[str, Any], Optional[List[str]]]:
    """
    Возвращает кортеж из:
    - основного профиля (всегда словарь)
    - метаданных (может быть списком строк или None)
    """
    profile = {"id": user_id, "name": "Анна"}
    metadata = ["preferences", "history"] if include_metadata else None
    return profile, metadata

"""
Задачи
"""

# 1. Написать функцию для вычисления возраста пользователя в этом году,
#    аннотировать типы, вызвать правильно и с ошибкой

def age(birth_year: int, cur_year: int = 2025) -> int:
    return cur_year - birth_year

print(age(2002))
#print(age('2002'))

# 2. Написать функцию, которая принимает имя, возраст и список хобби
#    пользователя. Функция возвращает словарь
def bio(
        name: str, 
        age: int, 
        hobbies: str
        ) -> Dict[str, Any]:
    return {"name": name, "age": age, "hobbies": hobbies.split(', ')}

print(bio("Polina", age(2002), "programming, music, series"))
#print(bio(1, 2, 3))

