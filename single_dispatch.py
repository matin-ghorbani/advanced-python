from functools import singledispatch


@singledispatch
def add(x: int, y: int) -> int:
    return x + y


@add.register
def _(x: str, y: str) -> str:
    return x + y


@add.register
def _(x: list, y: list) -> list:
    return (*x, *y)


def main():
    print(add(1, 2))
    print(add('a', 'b'))
    print(add([1, 2], [3, 4]))


if __name__ == '__main__':
    main()
