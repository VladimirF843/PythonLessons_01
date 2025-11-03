def get_word_with_h():
    """
    Спрашивает пользователя ввести слово с буквой 'H' или  'h'
    """
    entered_word = ""
    while "h" not in entered_word and "H" not in entered_word:
        entered_word = input("Введите слово с буквой 'H' или 'h': ")

    return entered_word

# Применение:
word = get_word_with_h()
print(f"Вы ввели: {word}")