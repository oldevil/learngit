from countURL import countURL as c
from countURL_use_iteration import countURL as c_iter
from time import time

def cmpCountURL(iterlim=1):
    t1 = time()
    for i in range(iterlim):
        c()
    t2 = time()
    for i in range(iterlim):
        c_iter()
    t3 = time()
    print('countURL: %f\ncountURL_use_iteration: %f' % (t2 - t1, t3 - t2))
    
if __name__ == '__main__':
    while True:
        iterlim = input('iterlim: ')
        try:
            iterlim = int(iterlim)
        except ValueError:
            print('wrong input...try again')
        else:
            break
    cmpCountURL(iterlim)