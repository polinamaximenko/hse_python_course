# Задача: Создать менеджер задач с подкомандами
# Использование:
#   python todo.py add "Добавить интеграцию TG API"
#   python todo.py list --status pending
#   python todo.py complete 1
# Подкоманды: add, list, complete, delete

import argparse
import os
import json

class TaskManager:
    def __init__(self, filename = "tasks.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            self._save_data({"tasks": []})


    def _load_data(self):
        """Загружает список из файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
             print(f"Ошибка: файл '{self.filename}' не найден")
        except json.JSONDecodeError:
             print(f"Ошибка декодирования JSON")
        except Exception as e:
             print(f"Ошибка при чтении файла: {e}")


    def _save_data(self, data):
        """Сохраняет список в файл"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)


    def add_task(self, description: str):
        """Добавляет задачу в список"""
        data = self._load_data()
        task_id = len(data["tasks"]) + 1
        task = {
            "id": task_id,
            "description": description,
            "status": "pending"
        }
        data["tasks"].append(task)
        self._save_data(data)
        print(f"Добавлена задача {task_id}: '{description}'")


    def list_tasks(self, status: str = None):
        """Выводит список задач с учетом статуса"""
        data = self._load_data()
        tasks = data["tasks"]
        if not tasks:
            print("Нет задач")
        else:
            for task in tasks:
                if status and task["status"] != status:
                    continue
                print(f"{task['id']}. {task['description']}")


    def complete_task(self, task_id: int):
        """Помечает задачу как выполненную"""
        data = self._load_data()
        for task in data["tasks"]:
            if task["id"] == task_id:
                task["status"] = "completed"
                self._save_data(data)
                print(f"Задача {task_id} выполнена")
                return
        print(f"Задача {task_id} не найдена")


    def delete_task(self, task_id: int):
        """Удаляет задачу из списка"""
        data = self._load_data()
        for i, task in enumerate(data["tasks"]):
            if task["id"] == task_id:
                del data["tasks"][i]
                self._save_data(data)
                print(f"Задача {task_id} удалена")
                return
        print(f"Задача {task_id} не найдена")


    def operation(self, args):
        if args.command == "add":
            self.add_task(args.description)
        elif args.command == "list":
            self.list_tasks(args.status)
        elif args.command == "complete":
            self.complete_task(args.task_id)
        elif args.command == "delete":
            self.delete_task(args.task_id)


    def main(self):
        parser = argparse.ArgumentParser(
            description="Менеджер задач",
            epilog="""
                    Примеры использования:
                       python todo.py add "Добавить интеграцию TG API" # Добавление задачи в список
                       python todo.py list --status pending            # Вывод списка задач со статусом
                       python todo.py complete 1                       # Выполнить задачу
                       python todo.py delete 1                         # Удалить задачу
                   """
        )
        subparsers = parser.add_subparsers(dest="command", required=True)

        subparsers.add_parser("add").add_argument("description", type=str)
        subparsers.add_parser("list").add_argument("--status", type=str, choices=["pending", "completed"])
        subparsers.add_parser("complete").add_argument("task_id", type=int)
        subparsers.add_parser("delete").add_argument("task_id", type=int)

        args = parser.parse_args()
        self.operation(args)

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.main()

# Примеры применения:
#   python todo.py add "Добавить интеграцию TG API"
# >>> Добавлена задача 1: 'Добавить интеграцию TG API'

#   python todo.py list --status pending
# >>> 1. Добавить интеграцию TG API

#   python todo.py complete 1
# >>> Задача 1 выполнена

#   python todo.py delete 1
# >>> Задача 1 удалена