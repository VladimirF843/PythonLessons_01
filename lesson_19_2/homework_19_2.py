import requests
from urllib.parse import quote
import logging
import json

# Конфиг логера
logging.basicConfig(
    filename="flask_server_photo_logger.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
print("Результаты записываются в файл 'flask_server_photos_logger.log'")


class ImageClient:

    def __init__(self, base_url: str):
        self._base_url = base_url

    # 1. POST-запрос
    def upload_image(self, image_path: str):
        print(f"\n--- Загрузка файла {image_path} ---")
        try:
            with open(image_path, 'rb') as image_file:
                files_to_send = {"image": image_file}
                url = f"{self._base_url}/upload"

                response = requests.post(url, files=files_to_send)
                response.raise_for_status()  # Проверяем, успешен ли запрос

                data = response.json()
                image_url = data.get("image_url")

                logging.info(f"Загрузка успешна! URL: {image_url}")
                return image_url

        except FileNotFoundError:
            logging.error(f"Файл не найден: {image_path}")
            return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Ошибка запроса POST: {e}")
            return None
        except json.JSONDecodeError:
            logging.error(f"Сервер вернул неверный формат ответа (не JSON).")
            return None

    # 2. GET-запрос
    def get_image(self, filename: str):
        print(f"\n--- Получение файла {filename} ---")
        try:
            encoded_filename = quote(filename, safe="")
            url = f"{self._base_url}/image/{encoded_filename}"

            response = requests.get(url)
            response.raise_for_status()  # Проверяем, успешен ли запрос

            content_type = response.headers.get("Content-Type", "")
            logging.info(f"Получен Content-Type: {content_type}")

            if "json" in content_type or content_type.startswith("text"):
                # Если сервер вернул ссылку (URL)
                data = response.json()
                image_url = data.get("image_url")
                logging.info(f"Получена ссылка: {image_url}")
                return image_url

            elif content_type.startswith("image"):
                # Сервер вернул сам файл изображения, сохраняем локально
                local_filename = "downloaded_" + filename
                with open(local_filename, "wb") as local_file:
                    local_file.write(response.content)
                logging.info(f"Изображение сохранено локально как: {local_filename}")
                return local_filename

            else:
                logging.error(f"Неподдерживаемый тип ответа: {content_type}")
                return None

        except requests.exceptions.RequestException as e:
            logging.error(f"Ошибка запроса GET: {e}")
            return None

    # 3. DELETE-запрос
    def delete_image(self, filename: str):
        print(f"\n--- Удаление файла {filename} ---")
        try:
            encoded_filename = quote(filename, safe="")
            url = f"{self._base_url}/delete/{encoded_filename}"

            response = requests.delete(url)
            response.raise_for_status()

            # Ожидаем JSON с подтверждением
            data = response.json()
            logging.info(f"Изображение удалено! Ответ: {data}")
            return data

        except requests.exceptions.RequestException as e:
            logging.error(f"Ошибка запроса DELETE: {e}")
            return None


# Основная Часть Программы

server = ImageClient('http://127.0.0.1:8080')

# Указываем путь и имя файла для работы
FILE_PATH = r"/Users/fvv/Downloads"
FILE_NAME = "File_test_JPG.jpg"

# Загружаем изображение
upload_url = server.upload_image(FILE_PATH)

# Получаем изображение
if upload_url:
    get_result = server.get_image(FILE_NAME)

# Удаляем изображение
if upload_url:
    delete_result = server.delete_image(FILE_NAME)

print("\nРабота завершена. Подробности смотрите в файле 'flask_server_photos_logger.log'")