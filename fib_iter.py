import sys

def fib(n):
    result = [0,1,1]
    i = 3
    #print result[i-1] + result[i-2]

    while i <= n:
        result.append(result[i-1] + result[i-2])
        i = i + 1

    return result[n]

index = int(sys.argv[1])
print fib(index)





