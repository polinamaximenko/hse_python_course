# Задача: Создать менеджер задач с подкомандами
# Использование:
#   python todo.py add "Добавить интеграцию TG API"
#   python todo.py list --status pending
#   python todo.py complete 1
# Подкоманды: add, list, complete, delete

import argparse
import os
import json

todo_file = "todo.json"

def load_tasks():
    """Загружает файл со списком задач (если он существует)"""
    if os.path.exists(todo_file):
        with open(todo_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Сохраняет список задач в файл"""
    with open(todo_file, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2)


def add_task(description: str):
    """Добавляет задачу в список"""
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "description": description,
        "status": "pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Добавлена задача {task_id}: '{description}'")


def list_tasks(status: str = None):
    """Выводит список задач с учетом статуса"""
    tasks = load_tasks()
    if not tasks:
        print("Нет задач")

    for task in tasks:
        if status and task["status"] != status:
            continue
        print(f"{task['id']}. {task['description']}")


def complete_task(task_id: int):
    """Помечает задачу как выполненную"""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed"
            print(f"Задача {task_id} выполнена")
            save_tasks(tasks)
            return
    print(f"Задача {task_id} не найдена")


def delete_task(task_id: int):
    """Удаляет задачу из списка"""
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            print(f"Задача {task_id} удалена")
            save_tasks(tasks)
            return
    print(f"Задача {task_id} не найдена")


def main():
    parser = argparse.ArgumentParser(
        description="Менеджер задач",
        epilog="""
                Примеры использования:
                   python todo.py add "Добавить интеграцию TG API  # Добавление задачи в список
                   python todo.py list --status pending            # Вывод списка задач со статусом
                   python todo.py complete 1                       # Выполнить задачу
                   python todo.py delete 1                         # Удалить задачу
               """
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("add").add_argument("description", type=str)
    subparsers.add_parser("list").add_argument("--status", type=str, choices=["pending", "completed"])
    subparsers.add_parser("complete").add_argument("task_id", type=int)
    subparsers.add_parser("delete").add_argument("task_id", type=int)

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks(args.status)
    elif args.command == "complete":
        complete_task(args.task_id)
    elif args.command == "delete":
        delete_task(args.task_id)


if __name__ == "__main__":
    main()

# Примеры применения:
#   python todo.py add "Добавить интеграцию TG API"
# >>> Добавлена задача 1: 'Добавить интеграцию TG API'

#   python todo.py list --status pending
# >>> 1. Добавить интеграцию TG API

#   python todo.py complete 1
# >>> Задача 1 выполнена

#   python todo.py delete 1
# >>> Задача 1 удалена