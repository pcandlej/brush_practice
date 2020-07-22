if __name__ == '__main__':
    while True:
        try:
            n = input()
            line = input().split()
            maxStep = [1]
            for i in range(1, len(line)):
                res = 1
                for j in range(0, i):
                    if int(line[j]) < int(line[i]):
                        res = max(maxStep[j] + 1, res)
                maxStep.append(res)
            print(max(maxStep))
        except:
            break
