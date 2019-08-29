from time import time

def cmpReadReadlines():
    t1 = time()
    with open('bi_aiops_mul.log', 'r') as f:
        temp1 = f.read()
    t2 = time()
    with open('bi_aiops_mul.log', 'r') as f:
        temp2 = f.readlines()
    t3 = time()
    print('read: %f\nreadlines: %f' % (t2 - t1, t3 - t2))
    
if __name__ == '__main__':
    cmpReadReadlines()