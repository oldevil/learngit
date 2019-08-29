def countURL(file='bi_aiops.log', target='/api/bi/user/user_info/'):
    tempfile = open(file, 'r')
    temp = tempfile.readlines()
    tempfile.close()
    count = 0
    for i in temp:
        if target in i:
            count += 1
    return count
    
if __name__ == '__main__':
    print(countURL())