"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

（1 <= prices.length <= 105）
"""

def max_income(price_list):

    if len(price_list) == 1:
        return 0

    max_income = 0
    for index in range(len(price_list)):
        for j in range(index + 1, len(price_list)):
            if price_list[j] - price_list[index] > max_income:
                max_income = price_list[j] - price_list[index]
    return max_income


def max_income_get_min(price_list):

    if len(price_list) == 1:
        return 0

    max_income_num = 0
    for index in range(len(price_list)):
        max_num = max(price_list[index:])
        if price_list[index] < max_num and max_num - price_list[index] > max_income_num:
            max_income_num = max_num - price_list[index]

    return max_income_num


if __name__ == '__main__':
    price_list = [7, 1, 5, 3, 6, 4]
    # price_list = [7, 6, 4, 3, 1]
    # ret = max_income(price_list)
    ret = max_income_get_min(price_list)
    print(ret)