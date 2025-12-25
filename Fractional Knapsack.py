def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    value = 0

    for val, wt in items:
        if capacity == 0:
            break
        if wt <= capacity:
            value += val
            capacity -= wt
        else:
            value += val * (capacity / wt)
            capacity = 0
    return value

print(fractional_knapsack([(60,10),(100,20),(120,30)],50))
