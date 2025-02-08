from dataclasses import dataclass
from typing import Callable
from functools import partial

@dataclass
class Customer:
    name: str
    age: int

def send_email(customers: list[Customer], is_adult: Callable[[Customer], bool]) -> None:
    for customer in customers:
        print(f'Sending email to {customer.name}')
        if is_adult(customer):
            print(f'Sorry, {customer.name} is too young to receive emails\n')
        else:
            print(f'Email sent to {customer.name}\n')

def is_adult(customer: Customer, min_age: int) -> bool:
    return customer.age >= min_age

def main() -> None:
    customers = [
        Customer('John', 25),
        Customer('Jane', 15),
        Customer('Doe', 30),
        Customer('Alice', 10),
        Customer('Matin', 17),
    ]

    partial_is_adult = partial(is_adult, min_age=18)
    send_email(customers, partial_is_adult)

if __name__ == '__main__':
    main()
