"""
Strategy é um padrão de projeto comportamental que tem a intenção de definir
uma famílida de algoritmos, encapsular cada uma delas e torná-las
intercambiáveis. Strategy permite que o algoritmo varie independentemente
dos clientes que o utilizam.

Princípio do aberto/fechado(open/closed principle):
Entidade devem ser abertas para extensão, mas fechadas para modificação.
"""
from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @classmethod
    @abstractmethod
    def calculate(cls, value: float) -> float: pass


class TwentyPercentOff(DiscountStrategy):
    @classmethod
    def calculate(cls, value: float) -> float:
        return value - (value * 0.2)


class FiftyPercentOff(DiscountStrategy):
    @classmethod
    def calculate(cls, value: float) -> float:
        return value - (value * 0.5)


class NoDiscount(DiscountStrategy):
    @classmethod
    def calculate(cls, value: float) -> float:
        return value


class CustomDiscount(DiscountStrategy):
    discount = 1

    def __init__(self, discount: int) -> None:
        __class__.discount = discount / 100

    @classmethod
    def calculate(cls, value: float) -> float:
        return value - (value * cls.discount)


class Order:
    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self._total)


if __name__ == '__main__':
    order = Order(1000, TwentyPercentOff)
    print(order.total)
    print(order.total_with_discount)

    order2 = Order(1000, FiftyPercentOff)
    print(order2.total)
    print(order2.total_with_discount)

    order3 = Order(1000, NoDiscount)
    print(order3.total)
    print(order3.total_with_discount)

    order4 = Order(1000, CustomDiscount(100))
    print(order4.total)
    print(order4.total_with_discount)
