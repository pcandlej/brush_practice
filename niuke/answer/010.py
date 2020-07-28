if __name__ == '__main__':
    while True:
        try:
            n = 0
            for i in range(int(input())):
                pw, r = i * i, str(i)
                if r == str(pw)[-len(r):]:
                    n += 1
            print(n)
        except:
            break
