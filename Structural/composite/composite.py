"""
Composite é um padrão de projeto estrutural que permite que
você utilize a composição para criar objetos em estruturas
de árvores. O padrão permite aos clientes tratarem de maneira
uniforme objetos individuais(leaf) e composições de
objetos(composite).

IMPORTANTE: só aplique este padrão em uma estrutura que possa ser
representada em formado hieraŕquico(árvore).

No padrão compopsite, temos dois tipos de objetos:
Composite(que representa nós internos da árvore) e Leaf
(que representa nós externos da árvore).

Objetos Composite são objetos mais complexos e com filhos.
Geralmente, eles delegam trabalho para os filhos
usando um método em comum.
Objetos Leaf são objetos simples, da ponta e sem filhos.
Geralmente, são esses objetos que realizam o trabalho
real da aplicação.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    """ Component """
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass

    def remove(self, child: BoxStructure) -> None: pass


class Box(BoxStructure):
    """ Composite """
    def __init__(self, name) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        print(f'\n{self.name}:')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    """ Leaf """
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == '__main__':
    # Leaf
    camiseta1 = Product('camiseta1', 10.99)
    camiseta2 = Product('camiseta2', 15.99)
    camiseta3 = Product('camiseta3', 20.99)

    # Composite
    caixa_camiseta = Box('caixa de camiseta')
    caixa_camiseta.add(camiseta1)
    caixa_camiseta.add(camiseta2)
    caixa_camiseta.add(camiseta3)

    # Leaf
    smartphone1 = Product('galaxy', 499.99)
    smartphone2 = Product('iphone', 699.99)

    # Composite
    caixa_smartphone = Box('caixa de smartphones')
    caixa_smartphone.add(smartphone1)
    caixa_smartphone.add(smartphone2)

    # Composite
    caixa_grande = Box('caixa grande')
    caixa_grande.add(caixa_camiseta)
    caixa_grande.add(caixa_smartphone)

    caixa_grande.print_content()
    print(caixa_grande.get_price())
