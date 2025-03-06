# You are given the price of a stock for 
# n
# n days. Your task is figure out the highest profit you could have made 
# if you had bought the stock on one day and sold it on another day.

# Consider the following situation:

# Day	0	1	2	3	4	5	6	7
# Price	3	7	5	1	4	6	2	3
# Here the highest profit is 6 – 1 = 5, achieved by buying on day 3 and selling on day 5.

def profits(p):
    x = len(p)
    best = 0
    for i in range(x):
        for j in range(i+1, x):
            best = max(best, p[j] - p[i])
    return best

print(profits([3, 7, 5, 1, 4, 6, 2, 3]))


