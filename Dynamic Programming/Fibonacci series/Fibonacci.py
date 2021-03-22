'''
Recursive mode

def fib_recur(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)
'''

#Dynamic Programming mode

def fib_dynamic(n):
    series = [0, 1]
    
    for i in range(2, n):
        series.append(series[-1] + series[-2])
        
    return series[-1] + series[-2]
