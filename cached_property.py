from typing import Iterable
from statistics import stdev
from functools import cached_property

class Data:
    def __init__(self, numbers: Iterable[float]) -> None:
        self.numbers = numbers
    
    @cached_property
    def stdv(self):
        print('Testing our function')
        return stdev(self.numbers)


def main() -> None:
    sequence = [1, 2, 3, 4, 5]
    data = Data(sequence)
    print(data.stdv)
    print(data.stdv)
    print(data.stdv)

if __name__ == '__main__':
    main()
