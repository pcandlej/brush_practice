def myprint(str):
    if len(str) > 8:
        print(str[:8])
        myprint(str[8:])
    else:
        print(str.ljust(8, '0'))


if __name__ == '__main__':
    while True:
        try:
            c = int(input())
            arr = []
            for i in range(c):
                arr.append(input())
            for s in arr:
                myprint(s)
        except:
            break
