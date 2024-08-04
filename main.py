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
    name_project = input("Введите название проекта: ")
    create_folder(f"{name_project}/handlers")  # Создание папки
    create_folder(f"{name_project}/keyboards")  # Создание папки
    create_folder(f"{name_project}/system")  # Создание папки
    create_folder(f"{name_project}/setting")  # Создание папки

    create_file_with_extension(f'{name_project}/requirements', 'txt')  # Создание файла с расширением
    create_file_with_extension(f'{name_project}/README', 'md')  # Создание файла с расширением
    create_file_with_extension(f'{name_project}/main', 'py')  # Создание файла с расширением
    create_file_with_extension(f'{name_project}/', 'gitignore')  # Создание файла с расширением

    create_file_with_extension(f'{name_project}/system/dispatcher', 'py')  # Создание файла с расширением
    create_file_with_extension(f'{name_project}/setting/config', 'ini')  # Создание файла с расширением
    create_file_with_extension(f'{name_project}/handlers/handlers', 'py')  # Создание файла с расширением
    create_file_with_extension(f'{name_project}/keyboards/keyboards', 'py')  # Создание файла с расширением


if __name__ == '__main__':
    main()
