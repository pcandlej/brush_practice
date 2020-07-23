from collections import defaultdict

if __name__ == '__main__':
    while True:
        try:
            dd = defaultdict(list)
            s = input()
            res = ""
            for c in set(s):
                dd[s.count(c)].append(c)

            for i in sorted(dd.keys(), reverse=True):
                res += "".join(sorted(dd[i], key=ord))

            print(res)
        except:
            break
