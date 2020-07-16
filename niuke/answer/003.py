def rsort(chars):
    l = len(chars)
    s = ''
    for i in range(l):
        s = s + chars[l - i - 1]
    print(s)


if __name__ == '__main__':
    rsort(input())
