def maxProfit(prices):
    res=0
    l=prices[0]
    for price in prices:
        if price<l:
            l=price
        res=max(res,price-l)
    return res
