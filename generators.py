from typing import Generator


def echo_round() -> Generator[int, float, int]:
    res = yield
    while res:
        res = yield round(res)
    
    return 'OK'


def simpl_generator() -> Generator[str, None, None]:
    gen_str = 'Hello World'
    yield gen_str

    gen_str += '!'
    yield gen_str
    
def main() -> None:
    # for generator_str in simpl_generator():
    #     print(generator_str)

    echo = echo_round()
    print(next(echo))
    print(echo.send(3.1415))
    print(echo.send(2.7182))
    print(echo.send(1.4142))

    try:
        echo.send(.0)
    except StopIteration as e:
        print(e.value)

if __name__ == '__main__':
    main()
