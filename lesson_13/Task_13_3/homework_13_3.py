import xml.etree.ElementTree as ET
import logging


class XmlDataFinderSimple:
    """
    Класс для поиска данных
    """

    def __init__(self, file_name):
        self.file_name = file_name
        self.setup_logging()

    def setup_logging(self):

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
        )

    def find_group_data(self, target_number: str):

        try:
            # Парсимо файл без складного шляху
            tree = ET.parse(self.file_name)
            root = tree.getroot()
        except FileNotFoundError:
            logging.error(f"Ошибка: Файл '{self.file_name}' не найден в директории.")
            return
        except ET.ParseError as e:
            logging.error(f"Ошибка парсинга XML: {e}")
            return

        found = False


        for group_element in root.findall('group'):

            number_element = group_element.find('number')

            if number_element is not None and number_element.text == target_number:

                found = True
                logging.info(f"--- Знайдено дані для групи №{target_number} ---")

                timing_exbytes_element = group_element.find('timingExbytes')
                incoming_element = group_element.find('incoming')

                if timing_exbytes_element is not None:
                    logging.info(f"timingExbytes: {timing_exbytes_element.text}")
                else:
                    logging.info("timingExbytes: Значение не найдено.")

                if incoming_element is not None:
                    logging.info(f"incoming: {incoming_element.text}")
                else:
                    logging.info("incoming: Значения не найдены.")

                return

        if not found:
            logging.warning(f"Поиск завершен: Группа с номеро '{target_number}' не найдена.")


# Исполняем


XML_FILE_NAME = 'groups.xml'

TARGET_GROUP_ID = '1001'

# 1. Инстанс класс
processor = XmlDataFinderSimple(XML_FILE_NAME)

# 2. Ищем
processor.find_group_data(TARGET_GROUP_ID)