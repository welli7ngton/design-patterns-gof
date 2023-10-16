"""
Padrão que visa especificar os tipos de objetos a serem criados usando uma
instância-protótipo e criar novos objetos pela cópia desse protótipo.
"""
from __future__ import annotations
from copy import deepcopy


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


class Person(StringReprMixin):
    def __init__(self, fristname: str, lastname: str) -> None:
        self.firstname = fristname
        self.lastname = lastname
        self.addresses: list[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


if __name__ == '__main__':
    wellington = Person('Wellington', 'Silva')
    wellington.add_address(Address('Rua 1', '9986'))
    mari = wellington.clone()
    mari.firstname = 'Marília'
    print(wellington)
    print(mari)
