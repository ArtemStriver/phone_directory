"""Интерфейс"""
from database import save, get, update, find, delete


def main_view():
    while True:
        print(
            "Выберите действие:\n"
            "1 - Вывод постранично записей из справочника на экран\n"
            "2 - Поиск записей по одной или нескольким характеристикам\n"
            "3 - Добавление новой записи в справочник\n"
            "4 - Возможность редактирования записей в справочнике\n"
            "5 - Удалить запись\n"
            "6 - Выйти из программы\n"
        )
        choice = int(input(">>> "))
        if choice == 1:
            record_list_view()
        elif choice == 2:
            find_record_view()
        elif choice == 3:
            add_record_view()
        elif choice == 4:
            update_record_view()
        elif choice == 5:
            delete_record_view()
        elif choice == 6:
            print("Ещё увидимся.")
            exit()
        else:
            print("Неизвестная команда.")


def record_list_view():
    # TODO отобразить 5 записей, информацию о количестве записей, с помощью действий "листать" записи.
    page_start = 0
    page_end = 5
    while True:
        print(
            "Просмотр записей из справочника:\n"
            "1 - назад\n"
            "2 - вперед\n"
            "3 - выход в меню\n"
        )
        get(page_start, page_end)
        choice = int(input(">>> "))

        if choice == 1:
            if page_start - 5 < 0:
                page_start = 0
                page_end = 5
            else:
                page_start -= 5
                page_end -= 5
        elif choice == 2:
            page_start += 5
            page_end += 5
        elif choice == 3:
            main_view()
        else:
            print("Неизвестная команда.")


def add_record_view():
    while True:
        try:
            print(
                "Добавить запись в справочник:\n"
                "для добавления записи введите необходимые данные или нажмите 3 для выхода\n"
                "exit - выход в меню\n"
            )
            # TODO вынести в датакласс или типизированный класс
            data = {"фамилия": None,
                    "имя": None,
                    "отчество": None,
                    "название организации": None,
                    "телефон рабочий": None,
                    "телефон личный": None}
            for key in data.keys():
                input_value = input(f"{key} ")
                if input_value == "exit":
                    main_view()
                if input_value == "":
                    data[key] = None
                else:
                    data[key] = input_value
            save(data)
            # TODO доделать функцию
            print("Запись добавлена")
            main_view()
        except Exception as exc:
            print(exc)
            # TODO выводить кастомные исключения


def update_record_view():
    try:
        print(
            "Обновить данные записи в справочнике по ее id:\n"
            "для обновления записи введите ее id, затем необходимые данные или нажмите 3 для выхода\n"
            "exit - выход в меню\n"
        )
        # TODO вынести в датакласс или типизированный класс
        choice = input(">>> ")
        if choice == "exit":
            main_view()
        choice = int(choice)
        get(choice, choice + 1)
        data = {"фамилия": None,
                "имя": None,
                "отчество": None,
                "название организации": None,
                "телефон рабочий": None,
                "телефон личный": None}
        for key in data.keys():
            input_value = input(f"{key} ")
            if input_value == "exit":
                main_view()
            if input_value == "":
                data[key] = None
            else:
                data[key] = input_value
        update(choice, data)
        # TODO доделать функцию
        print("Запись обновлена\n")
        get(choice, choice + 1)
        main_view()
    except Exception as exc:
        print(exc)
        # TODO выводить кастомные исключения


def delete_record_view():
    try:
        print(
            "Удалить запись из справочника по ее id:\n"
            "Введите id записи для ее удаления или нажмите 3 для выхода\n"
            "exit - выход в меню\n"
        )
        # TODO вынести в датакласс или типизированный класс
        choice = input(">>> ")
        if choice == "exit":
            main_view()
        choice = int(choice)
        get(choice, choice + 1)
        delete(choice)
        # TODO доделать функцию
        print("Запись удалена\n")
        main_view()
    except Exception as exc:
        print(exc)
        # TODO выводить кастомные исключения


def find_record_view():
    try:
        print(
            "Поиск:\n"
            "для поиска введите необходимые характеристики или нажмите 3 для выхода\n"
            "3 - выход в меню\n"
        )
        # TODO вынести в датакласс или типизированный класс
        data = {"фамилия": None,
                "имя": None,
                "отчество": None,
                "название организации": None,
                "телефон рабочий": None,
                "телефон личный": None}
        for key in data.keys():
            input_value = input(f"{key} ")
            if input_value == "exit":
                main_view()
            if input_value == "":
                data[key] = None
            else:
                data[key] = input_value
        find(data)
        # TODO доделать функцию
        main_view()
    except Exception as exc:
        print(exc)
        # TODO выводить кастомные исключения
