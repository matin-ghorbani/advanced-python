class Human:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.full_info: str = f'{self.name}, {self.age}'
        self._address: str | None = None
    
    @property
    def address(self) -> str | None:
        return f'Address: {self._address}' if self._address else 'Address is not set yet'
    
    @address.setter
    def address(self, new_address: str) -> None:
        self._address = new_address
        print(f'Address is set to {new_address}')

    def __len__(self) -> int:
        return self.age


def main() -> None:
    obj: Human = Human('Matin Ghorbani', 17)
    print(obj.address)
    obj.address = 'Mashhad, Iran'
    print(obj.address)
    

if __name__ == '__main__':
    main()
