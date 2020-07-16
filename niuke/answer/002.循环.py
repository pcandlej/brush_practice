def getCubeRoot(input):
    a = input
    b = input / 2
    c = 0
    while True:
        power = pow(b, 3)
        if round(power, 4) == round(input, 4):
            return round(b, 1)
        elif power > input:
            a = b
            b = (b + c) / 2
        else:
            c = b
            b = (a + b) / 2


if __name__ == '__main__':
    print(getCubeRoot(float(input())))
