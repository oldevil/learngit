def countURL(file='bi_aiops.log', target='/api/bi/user/user_info/'):
    with open(file, 'r') as f:
        return f.read().count(target)
    
if __name__ == '__main__':
    print(countURL())