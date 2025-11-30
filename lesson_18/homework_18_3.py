import logging

# Модуль pytest не используется в коде, поэтому он удален.

# --- Настройка логирования ---
# Создание и настройка логгера. Все сообщения будут записаны в файл 'login_function.log'
logging.basicConfig(
    filename='function_events.log',  # Изменено имя файла для ясности
    level=logging.INFO,  # Уровень логирования: INFO и выше
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)
logger = logging.getLogger("app_logger")  # Создаем объект логгера


# --- Декоратор логирования ---
def logging_decorator(func):
    """Добавляет запись в лог о вызове функции и ее результате."""

    def wrapper(*args, **kwargs):
        logger.info(f"Вызов функции '{func.__name__}' с аргументами: {args, kwargs}")

        # Вызываем декорируемую функцию один раз
        result = func(*args, **kwargs)

        logger.info(f"Результат функции '{func.__name__}': {result}")
        return result

    return wrapper


# --- Декоратор обработки исключений ---
def exception_decorator(func):
    """Перехватывает TypeError и записывает ошибку в лог."""

    def wrapper(*args, **kwargs):
        try:
            # Вызываем декорируемую функцию один раз
            return func(*args, **kwargs)
        except TypeError as er:
            # Если возникла TypeError, записываем ее в лог и возвращаем None
            logger.error(f"Ошибка TypeError при выполнении '{func.__name__}': {er}")
            return None  # Возвращаем None при ошибке

    return wrapper


# --- Декорируемая функция ---

@logging_decorator
@exception_decorator
def reversed_list(input_list):
    """Возвращает список в обратном порядке."""
    i = 0
    new_list = []
    # len(list) - 1, потому что индексы начинаются с 0
    while i <= len(input_list) - 1:
        # Добавляем элемент, начиная с последнего
        new_list.append(input_list[-1 - i])
        i += 1
    return new_list


# --- Примеры использования ---

my_list = [1, 2, 3, 4, 5]
# Множество (set) вызовет TypeError, так как оно не поддерживает индексирование
error_data = {1, 2, 3, 4, 5}

print("--- Запуск функции с корректными данными ---")
reversed_list(my_list)

print("\n--- Запуск функции с некорректными данными (ожидаем ошибку в логе) ---")
reversed_list(error_data)