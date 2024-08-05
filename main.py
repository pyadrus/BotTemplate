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

    # Шаг 1: Создание файла и запись кода
    with open(f'{name_project}/system/dispatcher.py', 'w', encoding='utf-8') as file:
        code_lines = [
            'import configparser\n\n',
            'from aiogram import Bot, Dispatcher, Router\n',
            'from aiogram.fsm.storage.memory import MemoryStorage\n\n',
            'config = configparser.ConfigParser(empty_lines_in_values=False, allow_no_value=True)\n',
            'config.read("setting/config.ini")  # Чтение файла\n',
            'BOT_TOKEN = config["BOT_TOKEN"]["BOT_TOKEN"]\n\n',
            'bot = Bot(\n',
            '    token=BOT_TOKEN,\n',
            ')\n',
            'storage = MemoryStorage()  # Хранилище\n',
            'dp = Dispatcher(storage=storage)\n\n',
            'ADMIN_USER_ID = 535185511, 301634256\n\n',
            'router = Router()\n',
            'dp.include_router(router)\n'
        ]
        file.writelines(code_lines)

        # Шаг 2: Создание файла и запись кода
        with open(f'{name_project}/main.py', 'w', encoding='utf-8') as file:
            code_lines = [
                'import asyncio\n',
                'import logging\n',
                'import sys\n\n',

                'from loguru import logger\n',

                'from handlers.greeting_handlers import register_greeting_handler\n',
                'from system.dispatcher import dp, bot\n\n',

                'logger.add("logs/log.log", retention="1 days", enqueue=True)  # Логирование бота\n\n',

                'async def main() -> None:\n',
                '    await dp.start_polling(bot)\n',
                '    register_greeting_handler()\n\n',

                'if __name__ == "__main__":\n',
                '    logging.basicConfig(level=logging.INFO, stream=sys.stdout)\n',
                '    asyncio.run(main())\n\n',
            ]
            file.writelines(code_lines)

            # Шаг 3: Создание файла и запись кода
            with open(f'{name_project}/handlers/handlers.py', 'w', encoding='utf-8') as file:
                code_lines = [
                    'from aiogram.filters import CommandStart\n',
                    'from aiogram.types import Message\n',
                    'from loguru import logger\n\n',

                    'from system.dispatcher import bot, dp\n\n',

                    '@dp.message(CommandStart())\n',
                    'async def command_start_handler(message: Message) -> None:\n',
                    '    user_id = message.from_user.id\n',
                    '    user_name = message.from_user.username\n',
                    '    user_first_name = message.from_user.first_name\n',
                    '    user_last_name = message.from_user.last_name\n',
                    '    user_date = message.date.strftime("%Y-%m-%d %H:%M:%S")\n',
                    '    logger.info(f"{user_id} {user_name} {user_first_name} {user_last_name} {user_date}")\n',

                    '    sign_up_text = "Добро пожаловать"\n',
                    '    await bot.send_message(message.from_user.id, sign_up_text, disable_web_page_preview=True)\n\n',

                    'def register_greeting_handler():\n',
                    '    """Регистрируем handlers для бота"""\n',
                    '    dp.message.register(command_start_handler)  # Обработчик команды /start, он же пост приветствия 👋\n\n',

                ]
                file.writelines(code_lines)


if __name__ == '__main__':
    main()
