import requests
import logging
from requests.exceptions import RequestException, HTTPError

# --- Настройка логирования ---
logging.basicConfig(
    filename="nasa_mars_photos.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)
logger = logging.getLogger("nasa_downloader")


def download_mars_photos():
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

    logger.info("Начало загрузки фотографий Марса.")
    download_count = 0

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        photos = data.get('photos', [])

        if not photos:
            logger.warning("API вернул пустой список фотографий.")
            return

        for photo_data in photos:
            if download_count >= 2:
                break

            photo_url = photo_data.get("img_src")
            if not photo_url:
                continue

            photo_response = requests.get(photo_url, timeout=10)
            photo_response.raise_for_status()

            filename = f"mars_photo{download_count + 1}.jpg"

            with open(filename, "wb") as file:
                file.write(photo_response.content)

            logger.info(f"Фото {download_count + 1} успешно сохранено как {filename}.")
            download_count += 1

        logger.info(f"Загрузка завершена. Всего сохранено: {download_count} фото.")

    except HTTPError as e:
        logger.error(f"HTTP ошибка (статус {e.response.status_code}): {e}")
    except RequestException as e:
        logger.error(f"Сетевая ошибка при запросе: {e}")
    except KeyError:
        logger.error("Ошибка при разборе JSON: не найдена структура 'photos'.")
    except Exception as e:
        logger.error(f"Произошла непредвиденная ошибка: {e}")


download_mars_photos()