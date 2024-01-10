from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from copy import deepcopy


class Ingrdient(ABC):
    @abstractmethod
    def get_price(self) -> float: pass

    @abstractmethod
    def get_name(self) -> str: pass

    def __repr__(self) -> str:
        return f'{self.get_name(), self.get_price()}'


class Bread(Ingrdient):
    price = 1.00

    def get_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.__class__.__name__


class Sausage(Ingrdient):
    price = 1.00

    def get_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.__class__.__name__


class Bacon(Ingrdient):
    price = 2.00

    def get_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.__class__.__name__


class Egg(Ingrdient):
    price = 2.00

    def get_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.__class__.__name__


class PotatoSticks(Ingrdient):
    price = 1.00

    def get_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.__class__.__name__


class MashedPotatoes(Ingrdient):
    price = 2.00

    def get_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.__class__.__name__


class Cheese(Ingrdient):
    price = 2.00

    def get_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.__class__.__name__


class Hotdog:
    _name: str
    _ingredients: List[Ingrdient] = []

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> float:
        return self._name

    @property
    def ingedients(self) -> List[Ingrdient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name} ({self.price}) -> {self.ingedients}'


class SimpleHotdog(Hotdog):
    def __init__(self) -> None:
        self._name = self.__class__.__name__
        self._ingredients: List[Ingrdient] = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]


class SpecialHotdog(Hotdog):
    def __init__(self) -> None:
        self._name = self.__class__.__name__
        self._ingredients: List[Ingrdient] = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotatoes(),
            PotatoSticks(),
        ]


# Decorators
class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog) -> None:
        self.hotdog = hotdog

    @property
    def price(self) -> float:
        return self.hotdog.price

    @property
    def name(self) -> float:
        return self.hotdog.name

    @property
    def ingedients(self) -> List[Ingrdient]:
        return self.hotdog._ingredients


class GeneralDecorator(HotdogDecorator):
    def __init__(self, hotdog: Hotdog, ingredient: Ingrdient) -> None:
        self.hotdog = hotdog

        self._ingredient = ingredient
        self._ingredients = deepcopy(self.hotdog.ingedients)
        self._ingredients.append(self._ingredient)

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> float:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'

    @property
    def ingedients(self) -> List[Ingrdient]:
        return self._ingredients


if __name__ == '__main__':
    simple_hotdog = SimpleHotdog()
    bacon_simple_hotdog = GeneralDecorator(simple_hotdog, Bacon())
    bacon_simple_hotdog = GeneralDecorator(bacon_simple_hotdog, Bacon())
    bacon_simple_hotdog = GeneralDecorator(bacon_simple_hotdog, Egg())
    print(bacon_simple_hotdog)
