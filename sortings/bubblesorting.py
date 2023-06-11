# Bubble sorting

"""
Первая итерация
[5, 3, 8, 6, 7, 2]
Он сравнивает первые два элемента, и здесь 5> 3, а затем меняет их местами. Теперь у нас есть новый список –

[3, 5, 8, 6, 7, 2]

Во втором сравнении 5 <8, тогда происходит замена –

[3, 5, 8, 6, 7, 2]

В третьем сравнении 8> 6, элементы меняются местами –

[3, 5, 6, 8, 7, 2]

В четвертом сравнении 8> 7, элементы меняются местами –

[3, 5, 6, 7, 8, 2]

В пятом сравнении 8> 2, также нужно их поменять местами –

[3, 5, 6, 7, 2, 8]

На этом первая итерация завершена, и в конце мы получаем самый большой элемент. Теперь нам нужно len (list1) – 1

Вторая итерация
[3, 5, 6, 7, 2, 8] -> [3, 5, 6, 7, 2, 8] здесь, 3 <5, тогда свопинг не произошел

[3, 5, 6, 7, 2, 8] -> [3, 5, 6, 7, 2, 8] здесь, 5 <6, также своп не произошел

[3, 5, 6, 7, 2, 8] -> [3, 5, 6, 7, 2, 8] здесь, 6 <7, свопинг не производился

[3, 5, 6, 7, 2, 8] -> [3, 5, 6, 2, 7, 8] здесь 7> 2, происходит их перемена местами. Теперь

[3, 5, 6, 2, 7, 8] -> [3, 5, 6, 2, 7, 8] здесь 7 <8, то свопинг не производится.

Третья итерация
[3, 5, 6, 2, 7, 8] -> [3, 5, 6, 7, 2, 8] здесь, 3 <5, тогда свопинг не производился

[3, 5, 6, 2, 7, 8] -> [3, 5, 6, 7, 2, 8] здесь, 5 <6, также свопинг не производился

[3, 5, 6, 2, 7, 8] -> [3, 5, 2, 6, 7, 8] здесь, 6 <2, поменяйте местами их позиции

[3, 5, 2, 6, 7, 8] -> [3, 5, 2, 6, 7, 8] здесь 6 <7, то свопинг не производится. Теперь

[3, 5, 2, 6, 7, 8] -> [3, 5, 2, 6, 7, 8] здесь 7 <8, необходимо поменять их местами.

Алгоритм будет повторяться, пока список не будет отсортирован.

Четвертая итерация
[3, 5, 2, 6, 7, 8] -> [3, 5, 2, 6, 7, 8]

[3, 5, 2, 6, 7, 8] -> [3, 2, 5, 6, 7, 8]

[3, 2, 5, 6, 7, 8] -> [3, 2, 5, 6, 7, 8]

[3, 2, 5, 6, 7, 8] -> [3, 2, 5, 6, 7, 8]

[3, 2, 5, 6, 7, 8] -> [3, 2, 5, 6, 7, 8]

Пятая итерация
[3, 2, 5, 6, 7, 8] -> [2, 3, 5, 6, 7, 8]
Мы видим, что наш список отсортирован с использованием метода пузырьковой сортировки.
"""
from typing import List, Union


class BubbleSorting:

    def __init__(self, sequence):
        """Constructor"""
        self.sequence = sequence

    @staticmethod
    def MyBubbleSorting(sequence: List[Union[int, float]]) -> List[Union[int, float]]:
        """
        :param sequence: sequence with int numbers
        :type sequence: List[Union[int, float]
        :return sequence: sequence with sorted int numbers
        :rtype sequence: List[Union[int, float]
        """
        for i in range(0, len(sequence)):
            for j in range(0, len(sequence) - 1):
                if sequence[j] > sequence[j + 1]:
                    tmp = sequence[j + 1]
                    sequence[j + 1] = sequence[j]
                    sequence[j] = tmp
        return sequence


lst = [[5, 3, 8, 6, 7, 2], [5.1, 3.3, 3.4, 4.4, 4.35]]

for i in range(len(lst)):
    result = BubbleSorting(sequence=lst).MyBubbleSorting(sequence=lst[i])
    print(result)
