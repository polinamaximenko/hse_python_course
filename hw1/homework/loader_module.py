import numpy as np
import pandas as pd
import os

class DataLoader():
    def __init__(self):
        self.data = None

    def _validate_file_path(self, file_path : str = 'data.csv'):
        """Проверяет существование пути файла и то, что это файл (а не директория)"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл '{file_path}' не существует")
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"'{file_path}' является директорией, а не файлом")

    def load_data(self, file_path : str = 'data.csv'):
        """Загружает данные и возвращает в формате DataFrame"""
        self._validate_file_path(file_path)
        self.data = pd.read_csv(file_path)
        return self.data

    def get_basic_info(self):
        """Выводит базовую информацию о датасете: форму (shape), имена колонок и количество пропущенных значений в каждой колонке"""
        if self.data is not None:
            shape = self.data.shape
            columns_lst = self.data.columns.to_list()
            nulls_lst = [int(self.data[c].isnull().sum()) for c in columns_lst]
            return f"Форма датасета: {shape}\nНазвания колонок: {columns_lst}\nКоличество пропущенных значений по колонкам: {nulls_lst}"
        else:
            raise ValueError("Данные не загружены")

