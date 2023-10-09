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


class VeiculoFactory(Veiculo):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

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

    def buscar_cliente(self) -> None:
        self.carro.buscar_cliente()


if __name__ == '__main__':
    carro = VeiculoFactory('Luxo')
    carro.buscar_cliente()
    moto = VeiculoFactory('Moto')
    moto.buscar_cliente()
