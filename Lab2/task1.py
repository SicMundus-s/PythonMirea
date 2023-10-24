import random


random_numbers = [random.randint(-10, 10) for _ in range(5)]


print("Исходный список:", random_numbers)


average = sum(random_numbers) / len(random_numbers)
print("Среднее арифметическое:", average)


random_numbers.reverse()
print("Список в обратном порядке:", random_numbers)


negative_numbers = [num for num in random_numbers if num < 0]
print("Список отрицательных элементов:", negative_numbers)