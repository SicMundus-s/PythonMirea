import re

def reverseWord(word):
    return word[::-1]


userInput = input("Введите произвольную строку: ")

pattern = r'\b[АЕИОУЫЭЮЯаеиоуыэюя][А-Яа-я]*\b'  # r'\b[АЕИОУЫЭЮЯаеиоуыэюя][А-Яа-я]*\b' - для английских

matches = re.findall(pattern, userInput)

reversed_words = [reverseWord(word) for word in matches]


print("Слова, начинающиеся с гласных букв:", matches)
