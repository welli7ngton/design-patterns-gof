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


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print(f'{__class__.__name__} está indo buscar o cliente...')


class VeiculoFactory(Veiculo):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'Luxo':
            return CarroLuxo()
        if tipo == 'Popular':
            return CarroPopular()
        if tipo == 'Moto':
            return Moto()


if __name__ == '__main__':
    moto = VeiculoFactory.get_carro('Moto')
    carro = VeiculoFactory.get_carro('Luxo')
    carro.buscar_cliente()
    moto.buscar_cliente()
