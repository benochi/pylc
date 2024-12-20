def stockPriceArr(prices):
    if not prices:
        return 0
    min_price1, max_profit1 = float('inf'), 0
    min_price2, max_profit2 = float('inf'), 0

    for price in prices:
        # First transaction
        min_price1 = min(min_price1, price)
        max_profit1 = max(max_profit1, price - min_price1)

        # Second transaction
        min_price2 = min(min_price2, price - max_profit1)
        max_profit2 = max(max_profit2, price - min_price2)

    return max_profit2


print(stockPriceArr(prices = [3, 3, 5, 0, 0, 3, 1, 4]))