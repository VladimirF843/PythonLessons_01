import unittest
import os
import logging
# Импортируем вашу функцию
from homework_10 import log_event

# Имя файла, которое использует оригинальная функция
TEST_LOG_FILE = 'login_system.log'


class TestLogEvent(unittest.TestCase):

    def setUp(self):
        """Очистка перед тестом: удаление файла и сброс логгера."""
        if os.path.exists(TEST_LOG_FILE):
            os.remove(TEST_LOG_FILE)

        logging.shutdown()
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

    def tearDown(self):
        """Очистка после теста: удаление файла."""
        if os.path.exists(TEST_LOG_FILE):
            os.remove(TEST_LOG_FILE)

    def _read_last_message(self):
        """Вспомогательная функция для чтения сообщения из файла."""
        if not os.path.exists(TEST_LOG_FILE):
            return ""

        with open(TEST_LOG_FILE, 'r') as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1].strip()
                # Отсекаем дату и время, чтобы получить чистое сообщение
                return last_line.split(' - ', 1)[1]
            return ""

    # --- ТЕСТЫ ---

    def test_success(self):
        """Проверяет лог для 'success' (INFO)."""
        username = "ok"
        status = "success"
        expected_msg = f"Login event - Username: {username}, Status: {status}"

        log_event(username, status)

        self.assertEqual(self._read_last_message(), expected_msg)

    def test_expired(self):
        """Проверяет лог для 'expired' (WARNING)."""
        username = "old"
        status = "expired"
        expected_msg = f"Login event - Username: {username}, Status: {status}"

        log_event(username, status)

        self.assertEqual(self._read_last_message(), expected_msg)

    def test_failed(self):
        """Проверяет лог для 'failed' (ERROR)."""
        username = "fail"
        status = "failed"
        expected_msg = f"Login event - Username: {username}, Status: {status}"

        log_event(username, status)

        self.assertEqual(self._read_last_message(), expected_msg)

    def test_unknown_status(self):
        """Проверяет лог для неизвестного статуса (ERROR)."""
        username = "unknown"
        status = "locked"
        expected_msg = f"Login event - Username: {username}, Status: {status}"

        log_event(username, status)

        self.assertEqual(self._read_last_message(), expected_msg)


if __name__ == '__main__' :
    unittest.main()