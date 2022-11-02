
def mysum(*args): # the number of arguments (splat operator *) return a tuple
    total = 0
    for a in args:
        total += a
    print(f'the sum is {total}')

mysum(1,2,3,4,5)
    
mysum(1,2,3)
mysum(1,2,3,4)
mysum(1,2)

mysum(*[1,2,3,4,5,6,7,8,9,10]) # Turning iterables into arguments