a, b = 9, 10
'''
normal if condition but having extra ordinary feature that we can insert values into string by using {} and format() method.
'''
if a > b:
    print("a({}) is greater than b({})".format(a, b))
else:
    print("a({}) is less than b({})".format(a, b))

'''
One more condition like ternary operator in java, it reflect python like below
'''

print("left" if a > b else "right")