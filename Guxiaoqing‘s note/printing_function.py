def print_odd(num):
    count = 0
    for i in range(1,num+1):
        if i%2!=0:
            print(i,end=' ')#以空格隔开
            count=count+1
        if count%10==0:
            print()