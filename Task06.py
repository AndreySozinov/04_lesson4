# Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def sum_func(numbers: list[float], index1: int, index2: int) -> float:
    result = 0
    for i in range(min(index1, index2) + 1, max(index1, index2)):
        if i < 0 or i >= len(numbers):
            continue
        else:
            result += numbers[i]
    return result


my_numbers = [3.3, 5, 17, 6.5, 2, 1]
index_first = int(input('Input first index: '))
index_second = int(input('Input second index: '))

print(f'Sum = {sum_func(my_numbers, index_first, index_second)}')
