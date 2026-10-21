def s_highest(x):
    highest = second = float('-inf')
    for i in x:
        if i > highest:
            second = highest
            highest = i
        elif highest > i > second:
            second = i
    return second