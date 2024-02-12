import database
from main import main

"""Модуль, организующий внутренний интерфейс программы."""


def record_list_view() -> None:
    """Функция для отображения логики просмотра записей."""
    page_start = 0
    page_end = 5
    while True:
        print(
            "Просмотр записей из справочника:\n"
            "1 - назад\n"
            "2 - вперед\n"
            "exit - выход в меню\n"
        )
        database.get(page_start, page_end)

        choice = input(">>> ")

        if choice == "exit":
            main()
        elif int(choice) == 1:
            if page_start - 5 < 0:
                page_start = 0
                page_end = 5
            else:
                page_start -= 5
                page_end -= 5
        elif int(choice) == 2:
            page_start += 5
            page_end += 5
        else:
            print("Неизвестная команда.")


def add_record_view() -> None:
    """Функция для отображения логики добавления записей."""
    print(
        "Добавить запись в справочник:\n"
        "Для добавления записи введите необходимые данные\n"
        "Для выхода в главное меню, ведите exit\n"
    )
    data = _data_generation()
    database.save(data=data)
    print("\nЗапись добавлена\n")
    main()


def update_record_view() -> None:
    """Функция для отображения логики обновления записи."""
    print(
        "Обновить данные записи в справочнике по ее id:\n"
        "\nДля обновления записи введите ее id, затем необходимые данные\n"
        "Для выхода в главное меню, ведите exit\n"
    )
    choice = input(">>> ")
    if choice == "exit":
        main()
    choice = int(choice)
    database.get(page_start=choice, page_end=choice + 1)

    data = _data_generation()
    database.update(data_id=choice, update_data=data)
    print("\nЗапись обновлена\n")

    database.get(page_start=choice, page_end=choice + 1)
    main()


def delete_record_view() -> None:
    """Функция для отображения логики удаления записи."""
    print(
        "Удалить запись из справочника по ее id:\n"
        "\nВведите id записи для ее удаления\n"
        "Для выхода в главное меню, ведите exit\n"
    )
    choice = input(">>> ")
    if choice == "exit":
        main()
    choice = int(choice)

    database.get(page_start=choice, page_end=choice + 1)
    database.delete(data_id=choice)
    print("Запись удалена\n")
    main()


def find_record_view() -> None:
    """Функция для отображения логики поиска записей."""
    print(
        "Поиск:\n"
        "\nДля поиска введите необходимые данные\n"
        "Для выхода в главное меню, ведите exit\n"
    )
    data = _data_generation()
    print("Были найдены следующие записи:\n")
    database.find(data=data)
    main()


def _data_generation() -> dict:
    """Функция для формирования данных записи."""
    data = {"Фамилия": None,
            "Имя": None,
            "Отчество": None,
            "Название организации": None,
            "Телефон рабочий": None,
            "Телефон личный": None}
    for key in data.keys():
        input_value = input(f"{key} ")
        if input_value == "exit":
            main()
        if input_value == "":
            data[key] = None
        else:
            data[key] = input_value
    return data
