class BaseFiboRange:

    def __init__(self, end_range, start_range=0):
        self._end_range = end_range
        self._start_range = start_range
        self._result_sequence = []

    def build_sequence(self):
        pass

    @staticmethod
    def _positive_sequence(end_range, start_range):
        fibo_sequence = [0, 1]
        result_sequence = []
        if start_range == 0:
            result_sequence.append(0)
        while fibo_sequence[-1] <= end_range:
            if fibo_sequence[-1] >= start_range:
                result_sequence.append(fibo_sequence[-1])
            fibo_sequence.append(fibo_sequence[-1] + fibo_sequence[-2])
        return result_sequence


class FibonacciRangePositive:
    def get_negative_sequence(self):
        return self._negative_sequence(end_range=self._start_range,
                                                            start_range=self._end_range)


class FibonacciRangeNegative:

    def get_negative_sequence(self):
        return self._negative_sequence(end_range=self._start_range,
                                                            start_range=self._end_range)

    def _negative_sequence(self, end_range, start_range=0):
        negative_sequence = self._positive_sequence(start_range=-start_range,
                                                    end_range=-end_range)
        for i in range(len(negative_sequence)):
            if i % 2 == 1:
                negative_sequence[i] = -negative_sequence[i]
        negative_sequence.reverse()
        return negative_sequence


class FibonacciRangeMixed:

    def get_mixed_sequence(self):
        return (
                self._negative_sequence(start_range=1, end_range=self._start_range)
                + self._positive_sequence(start_range=0,
                                          end_range=self._end_range)
            )


class FibonacciResultRange(BaseFiboRange,
                           FibonacciRangeNegative,
                           FibonacciRangePositive,
                           FibonacciRangeMixed):
    def build_sequence(self):
        if self._start_range < 0 and self._end_range <= 0:
            return self.get_negative_sequence()
        if self._start_range < 0 < self._end_range:
            return self.get_mixed_sequence()
        return self._positive_sequence(self._end_range, self._start_range)


class FibonacciRange:
    def __init__(self, end_range, start_range=0):
        self._end_range = end_range
        self._start_range = start_range
        self._result_sequence = []

    def build_sequence(self):
        if self._start_range < 0 and self._end_range <= 0:
            self._result_sequence = self._negative_sequence(end_range=self._start_range,
                                                            start_range=self._end_range)
        elif self._start_range < 0 < self._end_range:
            self._result_sequence = (
                self._negative_sequence(start_range=1, end_range=self._start_range)
                + self._positive_sequence(start_range=0,
                                          end_range=self._end_range)
            )
        else:
            self._result_sequence = self._positive_sequence(self._end_range, self._start_range)
        return self._result_sequence

    def _negative_sequence(self, end_range, start_range=0):
        negative_sequence = self._positive_sequence(start_range=-start_range,
                                                    end_range=-end_range)
        for i in range(len(negative_sequence)):
            if i % 2 == 1:
                negative_sequence[i] = -negative_sequence[i]
        negative_sequence.reverse()
        return negative_sequence

    @staticmethod
    def _positive_sequence(end_range, start_range):
        fibo_sequence = [0, 1]
        result_sequence = []
        if start_range == 0:
            result_sequence.append(0)
        while fibo_sequence[-1] <= end_range:
            if fibo_sequence[-1] >= start_range:
                result_sequence.append(fibo_sequence[-1])
            fibo_sequence.append(fibo_sequence[-1] + fibo_sequence[-2])
        return result_sequence


if __name__ == '__main__':
    a = FibonacciRange(start_range=-30, end_range=30)
    a_sequence = a.build_sequence()
    print(a_sequence)
