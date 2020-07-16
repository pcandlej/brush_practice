def dv(lt, rt, md, tg):
    power = md * md * md
    if round(power, 4) == round(tg, 4):
        return round(md, 1)
    elif power > tg:
        return dv(lt, md, (md + lt) / 2, tg)
    else:
        return dv(md, rt, (md + rt) / 2, tg)


def getCubeRoot(input):
    return dv(0, input, input / 2, input)


if __name__ == '__main__':
    print(getCubeRoot(float(input())))
