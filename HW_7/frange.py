from decimal import Decimal as D


class frange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            stop = start
            start = 0

        self._left = D(start)
        self._right = D(stop)
        self._step = D(step)

    def __next__(self):
        if (self._step > 0 and self._left >= self._right) or (self._step < 0 and self._left <= self._right):
            raise StopIteration

        result = self._left
        self._left += self._step
        return float(result)

    def __iter__(self):
        return self


for i in frange(1, 100, 3.5):
    print(i)




assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')
