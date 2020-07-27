def mysum(t):
    n, mysm = 2, 2
    for i in range(1, t):
        n += 3
        mysm += n
    return mysm


if __name__ == '__main__':
    while True:
        try:
            t = input()
            print(mysum(int(t)))
        except:
            break
