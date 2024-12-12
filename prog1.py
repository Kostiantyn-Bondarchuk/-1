import hashlib
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(message)s')


def hash_message_sha256(message: str) -> str:

    # Хешування рядка
    return hashlib.sha256(message.encode('utf-8')).hexdigest()


# Приклад використання
if __name__ == "__main__":
    try:
        input_message = input("Введіть повідомлення для хешування: ")
    except OSError:
        input_message = "Приклад повідомлення"
        logging.warning("Інтерактивне введення недоступне. Використано стандартне повідомлення.")

    hash_value = hash_message_sha256(input_message)
    logging.info(f"Геш-значення: {hash_value}")