
def nextChannel():
    yield 'b'
    yield 'a'
    
ch1 = nextChannel()
r = next(ch1)
print(r)
r = next(ch1)
print(r)