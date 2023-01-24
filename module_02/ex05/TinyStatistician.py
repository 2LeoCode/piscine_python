from math import sqrt


class TinyStatistician:
    def mean(self, v):
        if len(v) == 0:
            return None
        return float(sum(v) / len(v))

    def median(self, v):
        if len(v) == 0:
            return None
        return float(sorted(v)[len(v) // 2])

    def quartiles(self, v):
        if len(v) == 0:
            return None
        w = sorted(v)
        return float(w[len(w) // 4]), float(w[len(w) * 3 // 4])

    def var(self, v):
        if len(v) == 0:
            return None
        return float(sum((x - self.mean(v)) ** 2 for x in v) / len(v))

    def std(self, v):
        if len(v) == 0:
            return None
        return float(sqrt(self.var(v)))


if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]

    print(tstat.mean(a))
    # Expected result: 82.4

    print(tstat.median(a))
    # Expected result: 42.0

    print(tstat.quartiles(a))
    # Expected result: [10.0, 59.0]

    print(tstat.var(a))
    # Expected result: 12279.439999999999

    print(tstat.std(a))
    # Expected result: 110.81263465868862
