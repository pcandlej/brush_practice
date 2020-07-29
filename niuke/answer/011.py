from collections import defaultdict

if __name__ == '__main__':
    while True:
        try:
            s = input()
            isNum = s[0].isnumeric()
            dd = defaultdict(list)
            i = 0
            for c in s:
                if isNum == c.isnumeric():
                    dd[i].append(c)
                else:
                    isNum = c.isnumeric()
                    i += 1
                    dd[i].append(c)

            o = ""
            for n in range(0, i + 1):
                ss = "".join(dd[n])
                o += "*%s*" % ss if dd[n][0].isnumeric() else ss

            print(o)
        except:
            break

