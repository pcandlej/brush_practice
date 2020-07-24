if __name__ == '__main__':
    while True:
        try:
            cnt, ls, rvs = input(), map(int, input().split()), int(input())
            print(" ".join(map(str, sorted(ls, reverse=True if rvs == 1 else False))))
        except:
            break
