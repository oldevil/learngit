from time import time

def cmpCountIteration():
    with open('bi_aiops_mul.log', 'r') as f:
        temp1 = f.read()
        t1 = time()
        temp1.count('/api/bi/user/user_info/')
        t2 = time()
    with open('bi_aiops_mul.log', 'r') as f:
        temp2 = f.readlines()
        t3 = time()
        count = 0
        for i in temp2:
            if '/api/bi/user/user_info/' in i:
                count += 1
        t4 = time()
    print('count: %f\niteration: %f' % (t2 - t1, t4 - t3))
    
if __name__ == '__main__':
    cmpCountIteration()