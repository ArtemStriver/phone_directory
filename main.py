import views

"""Модуль, организующий основной интерфейс программы."""


def main():
    try:
        print("Программа phone_directory - это телефонный справочник со всем необходимым функционалом,\n"
              "используйте инструкции на экране для взаимодействия с ней.\n")
        while True:
            print(
                "Выберите действие:\n"
                "1 - Вывести постранично записи из справочника\n"
                "2 - Найти записи по одной или нескольким характеристикам\n"
                "3 - Добавить новую запись в справочник\n"
                "4 - Редактировать запись\n"
                "5 - Удалить запись\n"
                "6 - Выйти из программы\n"
            )
            choice = int(input(">>> "))
            if choice == 1:
                views.record_list_view()
            elif choice == 2:
                views.find_record_view()
            elif choice == 3:
                views.add_record_view()
            elif choice == 4:
                views.update_record_view()
            elif choice == 5:
                views.delete_record_view()
            elif choice == 6:
                print("Ещё увидимся!")
                exit(1)
            else:
                print("\nНеизвестная команда, попробуйте снова.\n")
    except Exception:
        print("\nНе удалось обработать команду! Программа будет перезапущена!\n")
        main()


if __name__ == "__main__":
    main()
