"""
TASK

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

from typing import List


def maxProfit_slow(prices: List[int]) -> int:
    res: list = []

    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > 0:
                res.append(prices[j] - prices[i])

    if len(res) > 0:
        return max(res)
    return 0


def maxProfit(prices: List[int]) -> int:
    """
    :type prices: List[int]
    :rtype: int
    """

    if not prices:
        return 0

    max_profit = 0
    # Первое значение принимаем за минимальную цену
    min_price = prices[0]

    for price in prices[1:]:
        # Прибыль = цена - минимальная цена
        profit = price - min_price
        # Создаем максимальную прибыль, если текущая прибыль > предыдущей (изначально 0)
        max_profit = max(max_profit, profit)
        # Присваиваем минимальной цене, минимальную цену
        min_price = min(min_price, price)

    return max_profit


pr = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]

for x in pr:
    res = maxProfit(prices=x)
    print(res)
