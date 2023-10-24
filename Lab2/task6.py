max_val = int(input("Введите целое число max_val: "))
repeat = int(input("Введите целое число repeat: "))

result_list = []

for i in range(1, max_val + 1):
    result_list.extend([i] * repeat)

print("Созданный список:", result_list)