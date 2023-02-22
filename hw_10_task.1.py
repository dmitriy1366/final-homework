"""
Каждое из слов «разработка», «сокет», «декоратор» представить в буквенном формате
и проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера
 преобразовать в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!) и также проверить тип
 и содержимое переменных.
"""


def word_format(lst):
    for elem in lst:
        print(f"{type(elem)}\n{elem}")


words = ['разработка', 'сокет', 'декоратор']
words_upoint = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                '\u0441\u043e\u043a\u0435\u0442',
                '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

word_format(words)
word_format(words_upoint)
