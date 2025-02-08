class Human:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __len__(self) -> int:
        return self.age


obj: Human = Human('Matin Ghorbani', 17)
print(len(obj))
