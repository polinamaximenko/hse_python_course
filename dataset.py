class Dataset:
    def __init__(self, filename):
        self.filename = filename
        self.data = self._read_file()
    def _read_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                text = file.read()
            return text.split('\n')
        except FileNotFoundError:
            print(f"Ошибка: файл '{self.filename}' не найден")
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")


dataset = Dataset('data.txt')
print(dataset.filename)
print(dataset.data[:5])