def dv(l, r, t, o):
    power = pow(t, 3)
    if round(power, 4) == round(o, 4):
        return round(t, 1)
    elif power > o:
        return dv(l, t, (t + l) / 2, o)
    else:
        return dv(t, r, (t + r) / 2, o)


def getCubeRoot(input):
    return dv(0, input, input / 2, input)


if __name__ == '__main__':
    print(getCubeRoot(float(input())))
