"""
Модуль, организующий взаимодействие с базой данных.
В качестве базы данных использован текстовый файл.
"""

database = "phone_directory.txt"


def formatter(data_dict: dict) -> str:
    """Преобразователь данных из словаря в строку."""
    data_str = str(data_dict)
    return data_str


def save(data: dict) -> None:
    """Функция для сохранения данных в файл."""
    with open(file=database, mode="a") as db:
        db.write(formatter(data) + "\n")


def get(page_start: int = 0, page_end: int = 5) -> str:
    """Функция для получения данных из файла, путем 'перелистывания' страниц."""
    with open(file=database, mode="r") as db:
        liens = [line for line in db]
        if page_end > len(liens):
            page_end = len(liens)
        for line in range(page_start, page_end):
            print(line, liens[line], end='')
    print()


def update(data_id: int, update_data: dict) -> None:
    """Функция для обновления данных записи."""
    with open(file=database, mode="r") as db:
        liens = [line for line in db]
        liens[data_id] = formatter(update_data)
    with open(file=database, mode='w') as db:
        for line in liens:
            db.write(line)


def delete(data_id: int) -> None:
    """Функция для удаления записи."""
    with open(file=database, mode="r") as db:
        liens = [line for line in db]
        liens.pop(data_id)
    with open(file=database, mode='w') as db:
        for line in liens:
            db.write(line)


def find(data: dict) -> str:
    """Функция для поиска записи в файле."""
    with open(file=database, mode="r") as db:
        liens = [line for line in db]
        need_lines = []
        for record in liens:
            for value in data.values():
                if value is not None and value in record:
                    need_lines.append(record)
                    break
        for line in need_lines:
            print(line, end="")
    print()
