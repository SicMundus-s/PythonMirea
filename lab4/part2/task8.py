import os
import concurrent.futures

def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

directory = 'D:/develop/'
files = [os.path.join(directory, file) for file in os.listdir(directory)]

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(count_words, files)

for file, result in zip(files, results):
    print(f"Файл: {file}, Количество слов: {result}")