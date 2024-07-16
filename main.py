import os


def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"Папка {folder_name} успешно создана")
    except FileExistsError:
        print(f"Папка {folder_name} уже существует")


def create_file_with_extension(file_name, extension):
    file_path = os.path.join(os.getcwd(), file_name + '.' + extension)
    with open(file_path, 'w') as f:
        print(f"Файл {file_path} успешно создан")


def main():
    create_folder("handlers")
    create_folder("keyboards")
    create_folder("system")
    create_folder("setting")
    create_file_with_extension('requirements', 'txt')
    create_file_with_extension('README', 'md')


if __name__ == '__main__':
    main()
