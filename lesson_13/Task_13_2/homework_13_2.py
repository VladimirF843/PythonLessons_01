import json
import logging
import os


class JsonReader:
    """
    Создаем класс
    """

    def __init__(self, files_list, log_path):
        self.files_to_read = files_list
        self.log_file_path = log_path
        self.setup_logging()

    def setup_logging(self):
        """
        КОнфиг логера
        """
        logging.basicConfig(
            filename=self.log_file_path,
            level=logging.ERROR,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filemode='w'
        )

    def read_and_log_errors(self):
        print("Начинаем читать файл...")

        for file_name in self.files_to_read:
            if not os.path.exists(file_name):
                logging.error(f"Не найдено файл: {file_name}")
                continue
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    data = json.load(f)

            except json.JSONDecodeError as e:
                logging.error(f"Ошибка декодирования в JSON {file_name}: {e}")

            except UnicodeError as e:
                logging.error(f"Ошибка кодировки в {file_name}: {e}")

            except Exception as e:
                logging.error(f"Неизвестная ошибка при работе с  {file_name}: {e}")

        print("Чтение завершено- проверьте логи.")



# Исполняем с вводными
jsonfiles = ('localizations_en.json', 'localizations_ru.json', 'login.json', 'login.json')
file_with_logs = 'json_logs.log'
json_processor = JsonReader(jsonfiles, file_with_logs)
json_processor.read_and_log_errors()