# -*- coding: utf-8 -*-
# quik sorting

"""
Делим массив пополам. Средний элемент — опорный.
Движемся от левого края массива вправо, до тех пор пока не обнаружим элемент, который больше опорного.
Движемся от правого края массива влево, до тех пор пока не обнаружим элемент, который меньше опорного.
Меняем местами два элемента, найденные в пунктах 2 и 3.
Продолжаем выполнять пункты 2-3-4, пока в результате обоюдного движения не произойдёт встреча.
В точке встречи массив делится на две части. К каждой части рекурсивно применяем алгоритм быстрой сортировки.

Почему это работает? Слева от точки встречи находятся элементы, меньшие или равные чем опорный.
Справа от точки встречи находятся элементы большие или равные чем опорный.
То есть, любой элемент из левой части меньше или равен любого элемента из правой части.
Поэтому в точке встречи массив можно смело поделить на два подмассива и аналогично рекурсивно сортировать каждый подмассив.
"""

from typing import List, Union


class QuikSorting:

    def __init__(self, sequence):
        """Constructor"""
        self.sequence = sequence

    @staticmethod
    def MyQuikSorting(sequence: List[Union[int, float]]) -> Union[List[Union[int, float]], int]:
        """
        :param sequence: sequence with int numbers
        :type sequence: List[Union[int, float]
        :return sequence: sequence with sorted int numbers
        :rtype sequence: List[Union[int, float]
        """
        less_elems: list = []
        more_elems: list = []
        pivoted_list: list = []

        if len(sequence) <= 1:
            return sequence
        else:
            pivoted_elem = sequence[0]

            for elem in sequence:
                if elem < pivoted_elem:
                    less_elems.append(elem)
                elif elem > pivoted_elem:
                    more_elems.append(elem)
                else:
                    pivoted_list.append(elem)

            # recursive
            less_elems = QuikSorting.MyQuikSorting(less_elems)
            more_elems = QuikSorting.MyQuikSorting(more_elems)
            return less_elems + pivoted_list + more_elems

    @staticmethod
    def MyQuikSort_with_filter_funk(sequence: List[Union[int, float]]) -> Union[List[Union[int, float]], int]:
        """
        :param sequence: sequence with int numbers
        :type sequence: List[Union[int, float]
        :return sequence: sequence with sorted int numbers
        :rtype sequence: List[Union[int, float]
        """
        if len(sequence) <= 1:
            return sequence

        unchor = sequence[0]
        less_elems = (list(filter(lambda x: x < unchor, sequence)))
        mid_elems = [i for i in sequence if i == unchor]
        more_elems = (list(filter(lambda x: x > unchor, sequence)))

        return QuikSorting.MyQuikSort_with_filter_funk(less_elems) + QuikSorting.MyQuikSort_with_filter_funk(mid_elems) + QuikSorting.MyQuikSort_with_filter_funk(more_elems)


lst = [[4, 1, 5, 90, 77, 3, 12, 0, 33, 31, 34, 35, 30], [5, 3, 8, 6, 7, 2], [5.1, 3.3, 3.4, 4.4, 4.35]]

for i in range(len(lst)):
    result = QuikSorting(sequence=lst).MyQuikSort_with_filter_funk(sequence=lst[i])
    print(result)
