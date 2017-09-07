# best time to buy and sell stock II

def solution(prices):
    if not prices:
        return 0
    buy, sell, profit = 0, 0, 0
    prices.append(0)
    while sell < len(prices)-1:
        if prices[sell] > prices[buy] and prices[sell+1] <= prices[sell]:
            profit += prices[sell] - prices[buy]
            buy = sell + 1
        elif prices[sell] > prices[buy] and prices[sell+1] > prices[sell]:
            sell += 1
            continue
        else:
            buy = sell
        sell += 1
    return profit

if __name__ == '__main__':
    print(solution([1,2,4]))