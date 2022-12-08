array = input("Введите последовательность чисел через пробел:").split()
number = int(input("Ведите число:"))

# 1. Преобразование введённой последовательности в список

array_list = list(map(int, array))

print('До сортировки')
print(array_list)

# 2. Сортировка списка по возрастанию элементов в нем

for i in range(len(array_list)):
    for j in range(len(array_list)-i-1):
        if array_list[j] > array_list[j+1]:
            array_list[j], array_list[j+1] = array_list[j+1], array_list[j]

print('После сортировки')
print(array_list)

# 3. Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу.

N = len(array_list)

def binary_search(array_list, number, left, right):
    if left > right: 
        return print('Числа нет в последовательности'), False

    middle = (right + left) // 2  
    if array_list[middle] == number:  
        return middle-1, middle 
    elif number < array_list[middle]:  
        return binary_search(array_list, number, left, middle - 1)
    else: 
        return binary_search(array_list, number, middle + 1, right)

print('''Hомер позиции элемента, который меньше введенного пользователем числа,
а следующий за ним больше или равен этому числу.''')

print(binary_search(array_list, number, 0, N - 1))
