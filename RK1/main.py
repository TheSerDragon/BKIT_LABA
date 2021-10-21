# используется для сортировки
from operator import itemgetter

class Prog:
    """Программа"""
    def __init__(self, id, name, price, comp_id):
        self.id = id
        self.name = name
        self.price = price
        self.comp_id = comp_id

class Comp:
    """Компьютер"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ProgComp:
    """
    'Программы компьютера' для реализации
    связи многие-ко-многим
    """
    def __init__(self, comp_id, prog_id):
        self.comp_id = comp_id
        self.prog_id = prog_id

# Компьютеры
comps = [
    Comp(1, 'компьютер Macbook'),
    Comp(2, 'компьютер Xiaomi'),
    Comp(3, 'компьютер Honor'),
    Comp(4, 'MSI'),

    Comp(11, 'компьютер (другой) Macbook'),
    Comp(22, '(другой) Xiaomi'),
    Comp(33, '(другой) Honor'),
    Comp(44, 'компьютер (другой) MSI'),
]

# Программы
progs = [
    Prog(1, 'Pycharm', 15000, 1),
    Prog(2, 'Visual Studio', 40000, 2),
    Prog(3, 'Inventor', 60000, 3),
    Prog(4, 'Access', 10000, 4),
    Prog(5, 'Workbench', 35000, 4),
]

progs_comps = [
    ProgComp(1, 1),
    ProgComp(2, 2),
    ProgComp(3, 3),
    ProgComp(4, 4),
    ProgComp(4, 5),

    ProgComp(11, 1),
    ProgComp(22, 2),
    ProgComp(33, 3),
    ProgComp(44, 4),
    ProgComp(44, 5),
]

def main():
    """Основная функция"""
    # Соединение данных один-ко-многим
    one_to_many = [(p.name, p.price, c.name)
                   for c in comps
                   for p in progs
                   if p.comp_id == c.id]
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, pc.comp_id, pc.prog_id)
                         for c in comps
                         for pc in progs_comps
                         if c.id == pc.comp_id]
    many_to_many = [(p.name, p.price, comp_name)
                    for comp_name, comp_id, prog_id in many_to_many_temp
                    for p in progs if p.id == prog_id]
    print('Задание 1')
    res_1 = sorted(one_to_many, key=itemgetter(2))
    # print(res_1)
    for i in res_1:
        print(i)
    print('\nЗадание 2')
    res_2_unsorted = []
    # Перебираем все компьютеры
    for c in comps:
        # Список программ компьютера
        c_progs = list(filter(lambda i: i[2] == c.name, one_to_many))
        # Если компьютер не пустой
        if len(c_progs) > 0:
            # Стоимость программ компьютера
            c_prices = [price for _, price, _ in c_progs]
            # Суммарная стоимость программ компьютера
            c_prices_sum = sum(c_prices)
            res_2_unsorted.append((c.name, c_prices_sum))
    # Сортировка по суммарной стоимости
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    # print(res_2)
    for i in res_2:
        print(i)
    print('\nЗадание 3')
    res_3 = {}
    # Перебираем все компьютеры
    for c in comps:
        if 'компьютер' in c.name:
            # Список программ компьютера
            c_progs = list(filter(lambda i: i[2] == c.name, many_to_many))
            # Только название программ
            c_progs_names = [x for x, _, _ in c_progs]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список названий
            res_3[c.name] = c_progs_names
    # print(res_3)
    for keys, values in res_3.items():
        print(keys, values)

if __name__ == '__main__':
    main()