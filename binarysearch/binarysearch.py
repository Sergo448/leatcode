# utf-8

# Binary search

"""
Этот алгоритм используется для поиска элемента в упорядоченной последовательности (например, списка, кортежа или строки).

Требования:
Чтобы применить алгоритм двоичного поиска к последовательности,
последовательность уже должна быть отсортирована в порядке возрастания.
В противном случае алгоритм не найдет правильный ответ. Если он найдет,
это будет чистым совпадением.

Совет: Вы можете отсортировать последовательность перед применением двоичного поиска с помощью алгоритма сортировки,
который соответствует вашим потребностям.

Ввод и вывод
Алгоритму (реализованному в виде функции) нужны эти данные:

Упорядоченная последовательность элементов (например: список, кортеж, строка).
Целевой элемент, который мы ищем.
Он возвращает индекс элемента, который вы ищете, если он найден. Если элемент не найден, возвращается значение -1.

Эффективность
Он очень эффективен по сравнению с линейным поиском (поиск элемента по одному, начиная с первого), 
потому что мы можем "отбрасывать" половину списка на каждом шаге.

Давайте начнем погружаться в этот алгоритм.

Визуальное пошаговое руководство
Мы применим алгоритм бинарного поиска к этому списку:
[1, 3, 4, 6, 24, 44, 65, 66, 87, 100]

Совет: Обратите внимание, что список уже отсортирован. Он включал индексы в качестве визуальной ссылки.

Цель
Мы хотим найти индекс целого числа 65.

Интервал
Давайте представим, что мы и есть алгоритм. Как нам запустить процесс?

Мы начинаем с выбора двух границ интервала, в котором мы хотим выполнить поиск.
Мы хотим выполнить поиск по всему списку,
поэтому мы выбираем index 0 в качестве нижней границы и index 8 в качестве верхней границы.


Средний элемент
Теперь нам нужно найти индекс среднего элемента в этом интервале. Мы делаем это, добавляя нижнюю границу 
и верхнюю границу и деля результат на 2 с помощью целочисленного деления.

В данном случае (0 + 9)//2 является  4 результатом 9/2 является 4.5, а целочисленное деление усекает десятичную часть.

Итак, средний элемент расположен с индексом 4, а средним элементом является число 24.

Сравнения
Теперь нам нужно начать сравнивать средний элемент с нашим целевым элементом, чтобы увидеть, что нам нужно делать дальше.

Мы просим:
Равен ли средний элемент элементу, который мы ищем?

24 == 65 # False
Нет, это не так.

Итак, мы спрашиваем:
Является ли средний элемент больше, чем элемент, который мы ищем?

24 > 65 # False
Нет, это не так.

Таким образом, средний элемент меньше, чем элемент, который мы ищем.

24 < 65 # True Отбрасывать элементы Поскольку список уже отсортирован, это говорит нам о чем-то чрезвычайно важном. 
Это говорит нам о том, что мы можем "отбросить" нижнюю половину списка, потому что мы знаем, что все элементы, 
которые идут перед средним элементом, будут меньше, чем элемент, который мы ищем, поэтому нашего целевого элемента 
там нет. 

Начните сначала - выберите границы
Что нам делать дальше? Мы отбросили элементы, и цикл повторяется снова.

Мы должны выбрать границы для нового интервала (см. Ниже). Но обратите внимание, что верхняя граница остается 
неизменной, и изменяется только нижняя граница. 

Это потому, что элемент, который мы ищем, может находиться в верхней половине списка. Верхняя граница 
остается неизменной, а нижняя граница изменяется, чтобы "сжать" интервал до интервала, в котором может быть найден 
наш целевой элемент. 

Совет: Если бы средний элемент был больше, чем элемент, который мы ищем, верхняя граница была бы изменена, 
а нижняя граница осталась бы неизменной. Таким образом, мы бы отбросили верхнюю половину списка и продолжили поиск в 
нижней половине. 

Средний элемент Теперь нам нужно найти индекс среднего элемента, добавив нижнюю границу к верхней границе и разделив 
результат на 2 с помощью целочисленного деления. 
 
Результатом (4+8)//2 является 6, таким образом, средний элемент расположен по индексу 6, а средний элемент равен 65.


Сравнения
Мы просим:
Равен ли средний элемент элементу, который мы ищем?

65 == 65 # True
Да, это так! Итак, мы нашли элемент с индексом 6. Возвращено значение 6, и алгоритм был успешно завершен.

💡 Совет: Если бы элемент не был найден, процесс продолжался бы до тех пор, пока интервал не стал бы 
недействительным. Если бы элемент не был найден во всем списке, было бы возвращено значение -1. """

from typing import List, Union


def binsearch(sequence: List[Union[int, float]], target: Union[int, float]) -> int:
    """
    
    :param sequence: sequence of elements
    :type sequence: List[Union[int, float]]
    :param target: int or float element
    :type target: int or float
    :return: index of target element in sequence
    :rtype index: int
    """
    sequence.sort()

    left: int = 0
    right: int = len(sequence) - 1

    while left <= right:
        middle = (left + right) // 2
        if sequence[middle] == target:
            return middle
        elif sequence[middle] < target:
            left = middle + 1
        elif sequence[middle] > target:
            right = middle - 1
        else:
            return -1

    return -1


arr = [1, 3, 4, 6, 24, 44, 65, 66, 87, 100]

print(binsearch(sequence=arr, target=65))
