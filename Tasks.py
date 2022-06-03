# 1.	Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя

def is_list_in_descending_order(nums_list):

    nums_list_in_descending_order = nums_list.copy()
    nums_list_in_descending_order.sort(reverse=True)

    return (nums_list == nums_list_in_descending_order)


def find_first_index_of_new_sequence(nums_list):
    number_index = 0

    while number_index < len(nums_list) - 1 and nums_list[number_index] >= numbers_list[number_index + 1]:
        number_index += 1

    return number_index


def create_ascending_list(nums_list, first_index):
    result_list = [nums_list[first_index]]

    for i in range(first_index + 1, len(nums_list)):
        if result_list[-1] < nums_list[i]:
            result_list.append(numbers_list[i])

    return result_list


# numbers_list = [- 2, 7, 7, 8, 6, 6, 5, 5, 10, 4, 3, 2, 1, 11]
numbers_list = [1, 5, 2, 3, 4, 6, 1, 7]


if not is_list_in_descending_order(numbers_list):
    print(f'В списке {numbers_list} одна из возрастающих последовательностей - {create_ascending_list(numbers_list, find_first_index_of_new_sequence(numbers_list))}')
else:
    print(
        f'Список {numbers_list} отсортирован по убыванию. Возрастающих последовательностей нет.')

#_____________________________________________________________________________________________________________________
# 2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.

import random


def generation_of_random_numbers_list(length, min_value, max_value):
    return [random.randint(min_value, max_value) for i in range(length)]


def write_numbers_list_to_file(file_name, separator, nums_list):
    with open(file_name, 'w') as data:
        data.write(separator.join(str(element) for element in nums_list))


def read_numbers_list_from_file(file_name, separator):
    result_list = []
    with open(file_name, 'r') as data:
        result_list = list(map(int, data.read().split(separator)))
    return result_list


file_name = 'file_task_2.txt'
separator = " "
numbers_list_to_file = []
numbers_list_from_file = []


numbers_list_to_file = generation_of_random_numbers_list(
    length=10, min_value=-100, max_value=100)
write_numbers_list_to_file(file_name, separator, numbers_list_to_file)

numbers_list_from_file = read_numbers_list_from_file(file_name, separator)
# print(numbers_list_from_file)
numbers_list_from_file.sort()
write_numbers_list_to_file(file_name, separator, numbers_list_from_file)

#_____________________________________________________________
# 3.	Вот вам файл с тысячей чисел. https://cloud.mail.ru/public/DQgN/LqoQzPEec
# Задача: найти триплеты и просто выводить их на экран. Триплетом называются три числа, которые в сумме дают 0.
# (решение будет долгим, ибо является демонстрационным при теме многопоточного программирования).

def read_numbers_list_from_file(file_name, separator):
    result_list = []
    with open(file_name, 'r') as data:
        for line in data:
            result_list.append(int(line.replace(separator, "").strip()))
    return result_list


def find_and_print_triplet_brute_force_method(nums_list):
    count = 0
    for i in range(len(nums_list) - 2):
        for j in range(i + 1, len(nums_list) - 1):
            for k in range(j + 1, len(nums_list)):
                if nums_list[i] + nums_list[j] + nums_list[k] == 0:
                    print(
                        f'{nums_list[i]} + {nums_list[j]} + {nums_list[k]} = 0')
                    count += 1
    print(f'Всего триплетов - {count}')


def find_and_print_triplet_set_method(nums_list):
    count = 0
    for i in range(len(nums_list)):
        set_check_numbers = set()
        for j in range(i + 1, len(nums_list)):
            if -(nums_list[i] + nums_list[j]) in set_check_numbers:
                print(
                    f'{nums_list[i]} + {nums_list[j]} + {-(nums_list[i] + nums_list[j])} = 0')
                count += 1
            else:
                set_check_numbers.add(nums_list[j])
    print(f'Всего триплетов - {count}')


file_name = 'file_task_3.txt'
separator = "\n"
numbers_list_from_file = [-1, 2, -2, 3, -3, 1]

numbers_list_from_file = read_numbers_list_from_file(file_name, separator)
print(numbers_list_from_file)

find_and_print_triplet_brute_force_method(numbers_list_from_file)
find_and_print_triplet_set_method(numbers_list_from_file)
