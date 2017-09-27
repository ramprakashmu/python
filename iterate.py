from builtins import range
def isEvenOdd(n):
    if n / 2 == 0:
        print('{} is even number'.format(n))
    else:
        print('{} is odd number'.format(n))
        
for n in range(1, 20):
    isEvenOdd(n)
