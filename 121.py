# best time to buy and sell stocks

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    back_p, front_p, gap = 0, 0, 0
    for front_p in range(len(prices)):
        if prices[front_p] - prices[back_p] > gap:
            gap = prices[front_p] - prices[back_p]
        if prices[front_p] < prices[back_p]:
            back_p = front_p
    return gap


if __name__ == '__main__':
    print(maxProfit([2,4,1]))