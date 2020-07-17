if __name__ == '__main__':
    ns = input().split()
    f, z, zc = 0, 0, 0

    for n in ns:
        n = int(n)
        if n < 0:
            f += 1
        else:
            z += 1
            zc += n

    print(f)
    print(round(zc/z, 1))
