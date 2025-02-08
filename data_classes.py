import random
import string
from dataclasses import dataclass, field


def gen_id() -> str:
    return ''.join(random.choices(string.ascii_letters, k=10))


# @dataclass(kw_only=True, frozen=True)
@dataclass(kw_only=True)
class Human:
    name: str
    address: str
    human_id: str = field(default_factory=gen_id, init=False, repr=False)
    full_info: str = field(init=False)
    emails: list = field(default_factory=list)

    def __post_init__(self):
        self.full_info = f'{self.name}, {self.address}'


def main() -> None:
    human = Human(name='Matin Ghorbani', address='Mashhad', emails=['matin.ghorbani101010@gmail.com'])
    print(human)

    # human.address = 'Tehran' # We get an error if `frozen = True`



if __name__ == '__main__':
    main()
