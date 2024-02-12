from views import main_view
"""Главный файл, объединяющий весь функционал."""


def main():
    try:
        main_view()
    except Exception as exc:
        print(exc)
        main()


if __name__ == "__main__":
    main()
