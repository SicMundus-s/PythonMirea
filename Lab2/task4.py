import random

list1 = [random.randint(1, 10) for _ in range(5)]
list2 = [random.randint(1, 10) for _ in range(5)]

print("Список 1:", list1)
print("Список 2:", list2)

unique_numbers_list1 = set(list1)
unique_numbers_list2 = set(list2)

count_unique_numbers_list1 = len(unique_numbers_list1)
count_unique_numbers_list2 = len(unique_numbers_list2)

print("Уникальные числа в списке 1:", count_unique_numbers_list1) # Уникальные числа это и есть различные числа
print("Уникальные числа в списке 2:", count_unique_numbers_list2)

common_numbers = set(list1) & set(list2)
count_common_numbers = len(common_numbers)

print("Количество общих чисел в обоих списках:", count_common_numbers)

common_numbers_sorted = sorted(common_numbers)

print("Общие числа в порядке возрастания:", common_numbers_sorted)

list1 = [x for x in list1 if x not in common_numbers]

print("Список 1 после удаления общих чисел:", list1)
