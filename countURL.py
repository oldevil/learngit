def countURL(file='bi_aiops.log', target='/api/bi/user/user_info/'):
    count = 0
    with open(file, 'r') as f:
        for i in f.readlines():
            if target in i:
                count += 1
    return count
    
if __name__ == '__main__':
    print(countURL())