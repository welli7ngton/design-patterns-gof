"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subcçasses decidirem quais objetos criar.
O Factory method permite adiar a instanciação para as subclasses, garantido o
baixo acoplamento entre classes.
"""
from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print(f'{__class__.__name__} está indo buscar o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print(f'{__class__.__name__} está indo buscar o cliente...')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print(f'{__class__.__name__} está indo buscar o cliente...')


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print(f'{__class__.__name__} está indo buscar o cliente...')


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass

    def buscar_cliente(self) -> None:
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'Luxo':
            return CarroLuxo()
        if tipo == 'Popular':
            return CarroPopular()
        if tipo == 'Moto':
            return Moto()
        if tipo == 'MotoLuxo':
            return MotoLuxo()


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'Popular':
            return CarroPopular()


if __name__ == '__main__':
    from random import choice

    veiculos_disponiveis_zona_norte = ['Luxo', 'Popular', 'Moto', 'MotoLuxo']
    veiculos_disponiveis_zona_sul = ['Popular']

    print('Zona norte:')
    for i in range(10):
        veiculo = ZonaNorteVeiculoFactory(
            choice(veiculos_disponiveis_zona_norte)
        )
        veiculo.buscar_cliente()

    print()

    print('Zona sul:')
    for i in range(10):
        veiculo = ZonaSulVeiculoFactory(
            choice(veiculos_disponiveis_zona_sul)
        )
        veiculo.buscar_cliente()
