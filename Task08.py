# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

parts = 50
shops = 2
numbers = [5, 2, 1]
texts = 'Something else'
s = 76.8
toad = '52'


def s_replace():
    """
    Значения меняются на None, но новые переменные не появляются. Если добавлять ключи в glob_dict выдает ошибку итерирования
    :return:
    """
    glob_dict = globals()
    new_glob_dict = glob_dict.copy()
    for key, value in new_glob_dict.items():
        if key.endswith('s') and len(key) > 1:
            glob_dict[key.replace('s', '')] = value
            glob_dict[key] = None


print(parts, s, shops, toad)
s_replace()
print(parts, s, shops, toad)
print(globals())
