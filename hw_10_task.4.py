"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

convert_words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in convert_words:
    word = word.encode('utf8')
    print(word)
    word = word.decode('utf8')
    print(word)
    print()
