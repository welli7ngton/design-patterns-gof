# flake8: noqa
from abc import ABC, abstractmethod


class Pizza(ABC):
    def prepare(self):
        # template method
        self.hook_before_add_ingredients()
        self.add_igredients()
        self.hook_after_add_ingredients()
        self.cook()
        self.cut()
        self.serve()

    def hook_before_add_ingredients(self): pass
    def hook_after_add_ingredients(self): pass

    def serve(self):
        print(f'Servindo a pizza: {self.__class__.__name__}.')
        print('--------------------------------------------------')

    @abstractmethod
    def add_igredients(self): pass

    @abstractmethod
    def cook(self): pass

    @abstractmethod
    def cut(self): pass


class StylishPizza(Pizza):
    def __init__(self, size: str) -> None:
        self._size = size

    def add_igredients(self):
        print(f'{self.__class__.__name__}: presunto, queijo, orégano, cebola.')

    def cook(self):
        print(f'{self.__class__.__name__}: cozinhando por 45 minutos no forno a lenha.')

    def cut(self):
        if self._size == 'L':
            print('cutting 8 piecies.')
        elif self._size == 'M':
            print('cutting 6 pieces.')
        else:
            print('cutting 4 pieces.')


class FourChesses(Pizza):
    def __init__(self, size: str) -> None:
        self._size = size

    def hook_before_add_ingredients(self):
        print(f'{self.__class__.__name__}: fatiando o queijo.')

    def add_igredients(self):
        print(f'{self.__class__.__name__}: cheddar, coalho, parmesão, provolone.')

    def cook(self):
        print(f'{self.__class__.__name__}: cozinhando por 20 minutos no forno a comum.')

    def cut(self):
        if self._size == 'L':
            print('cutting 8 piecies.')
        elif self._size == 'M':
            print('cutting 6 pieces.')
        elif self._size == 'S':
            print('cutting 4 pieces.')


if __name__ == '__main__':
    stylish = StylishPizza('L')
    stylish.prepare()

    fourcheses = FourChesses('S')
    fourcheses.prepare()
