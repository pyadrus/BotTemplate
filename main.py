import os


def create_folder(folder_name):
    """Создание папки"""
    try:
        os.makedirs(folder_name)
        print(f"Папка {folder_name} успешно создана")
    except FileExistsError:
        print(f"Папка {folder_name} уже существует")


def create_file_with_extension(file_name, extension):
    """Создание файла с расширением"""
    file_path = os.path.join(os.getcwd(), file_name + '.' + extension)
    with open(file_path, 'w') as f:
        print(f"Файл {file_path} успешно создан")


def main():
    create_folder("Новый_проект/handlers") # Создание папки
    create_folder("Новый_проект/keyboards") # Создание папки
    create_folder("Новый_проект/system") # Создание папки
    create_folder("Новый_проект/setting") # Создание папки

    create_file_with_extension('Новый_проект/requirements', 'txt') # Создание файла с расширением
    create_file_with_extension('Новый_проект/README', 'md') # Создание файла с расширением
    create_file_with_extension('Новый_проект/main', 'py') # Создание файла с расширением
    create_file_with_extension('Новый_проект/', 'gitignore')  # Создание файла с расширением

    create_file_with_extension('Новый_проект/system/dispatcher', 'py') # Создание файла с расширением
    create_file_with_extension('Новый_проект/setting/config', 'ini') # Создание файла с расширением
    create_file_with_extension('Новый_проект/handlers/handlers', 'py') # Создание файла с расширением
    create_file_with_extension('Новый_проект/keyboards/keyboards', 'py') # Создание файла с расширением


if __name__ == '__main__':
    main()
