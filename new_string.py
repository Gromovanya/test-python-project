# Это файл для чтения списка
# Есть список и он проходится по нему.
# Когда он находит строку он добавляет её.
# Выводит получившуюся строку из всех строковых значений и переворачивает её.

def new_string(in_string):
    new_str = ''
    for i in in_string:
        if isinstance(i, str):
            new_str += i

    return new_str[::-1]


if __name__ == '__main__':
    string_new = ['a',1,'g',3,'w',2,'e','a']
    print(new_string(string_new))