def stock_span_problem(prices):
    s = [] # Stack to store pairs (price, index)
    v= [] # To store the indices of the previous higher price
    size = len(prices)

    for i in range(size):
        if not s:
            v.append(-1)
        elif s[-1][0] > prices[i]:
            v.append(s[-1][1])
        else:
            while s and s[-1][0] <= prices[i]:
                s.pop()
            if not s:
                v.append(-1) # No previous greater element
            else:
                v.append(s[-1][1]) # Index of previous greater element
        s.append((prices[i],i)) # Push current price and index onto the stack
    
    for i in range(size):
        v[i] = i - v[i]
    return v

prices = [100, 80, 60, 70, 60, 75, 85]
print(stock_span_problem(prices)) #Outpu: [1, 1, 1, 2, 1, 4, 6]