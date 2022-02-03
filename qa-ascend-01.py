
def square(y):
    for i in range(1,y+1):
        print('x',end=' ')
        for k in range (2,y+1):
            if  k == y:
                print('x')
            elif k == i:
                print('x',end=' ')
            else:
                print('O', end=' ')

y = int(input("Please enter a number for Y : "))
square(y)