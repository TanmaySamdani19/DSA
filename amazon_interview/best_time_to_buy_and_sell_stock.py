def solution(prices):
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price: # Update min_price if current price is lower	
            min_price = price
        elif price - min_price > max_profit: # Check if current price minus min_price is greater than max_profit
            max_profit = price - min_price
    return max_profit