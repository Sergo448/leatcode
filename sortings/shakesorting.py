# -*- coding: utf-8 -*-
# Shake Sorting

"""
Разновидность пузырька. На первом проходе, как обычно — задвигаем максимум в конец.
Потом резко разворачиваемся и толкаем минимум в начало.
Отсортированные крайние области массива увеличиваются в размерах после каждой итерации.
"""
from typing import List, Union


class ShakeSorting:

    def __init__(self, sequence):
        """Constructor"""
        self.sequence = sequence

    @staticmethod
    def MyShakeSorting(sequence: List[Union[int, float]]) -> Union[List[Union[int, float]], int]:
        """
        :param sequence: sequence with int numbers
        :type sequence: List[Union[int, float]
        :return sequence: sequence with sorted int numbers
        :rtype sequence: List[Union[int, float]
        """
        #
        if len(sequence) == 0:
            return 1
        # Промежуток
        up = range(len(sequence) - 1)
        while True:
            # 2 промежутка в 1 цикле ([от 0 до -1] и [от -1 до 0])
            for indexes in (up, reversed(up)):
                # Инициализация переменной для выхода из цикла
                swapped: bool = False
                # Пока мы заходим в цикл мы идем туда обратно. Если ни разу не заходили - значит пора заканчивать
                for i in indexes:
                    if sequence[i] > sequence[i+1]:
                        sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
                        swapped = True
                # Если на последнем проходе туда-обратно ни разу не заходили в цикл - возвращаем отсортированный массив
                if not swapped:
                    return sequence


lst = [[4, 1, 5, 90, 77, 3, 12, 0, 33, 31, 34, 35, 30], [5, 3, 8, 6, 7, 2], [5.1, 3.3, 3.4, 4.4, 4.35]]

for i in range(len(lst)):
    result = ShakeSorting(sequence=lst).MyShakeSorting(sequence=lst[i])
    print(result)
