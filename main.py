import os


def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"Папка {folder_name} успешно создана")
    except FileExistsError:
        print(f"Папка {folder_name} уже существует")

    # Пример использования


create_folder("Новая папка")


def create_file_with_extension(file_name, extension):
    file_path = os.path.join(os.getcwd(), file_name + '.' + extension)
    with open(file_path, 'w') as f:
        f.write('Привет, мир!')


# Пример использования
create_file_with_extension('новый_файл', 'txt')
