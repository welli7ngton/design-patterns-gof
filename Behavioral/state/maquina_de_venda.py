# flake8: noqa
# Exercício Avançado de Refatoração usando o Padrão State

# Imagine um sistema de controle de uma máquina de venda automática que vende
# diferentes tipos de produtos. Cada produto pode ter um estado diferente
# como "Sem estoque", "Em estoque" e "Fora de serviço". Atualmente, o sistema
# é implementado sem o uso do padrão State, e a classe VendingMachine possui
# métodos para comprar produtos, reabastecer estoque, etc.

# Sua tarefa é refatorar o sistema usando o padrão State para lidar com
# os diferentes estados dos produtos de forma mais eficiente e extensível.

# Crie uma interface EstadoProduto que declare métodos para cada ação que
# um produto pode realizar, como comprar, reabastecer, etc.

# Implemente classes concretas que implementem essa interface para
# representar os diferentes estados dos produtos, por exemplo
# ProdutoSemEstoque, ProdutoEmEstoque e ProdutoForaDeServico.

# Modifique a classe Produto para ter uma referência para um objeto de
# estado atual, inicializado com o estado padrão(ProdutoEmEstoque, por exemplo)

# Atualize os métodos da classe Produto para delegar as chamadas de método
# para o objeto de estado atual.

# Modifique a classe VendingMachine para usar a nova implementação de
# produtos com o padrão State.

# Dica: Considere como os estados dos produtos podem interagir entre si e
# como você pode organizar a lógica para tornar o código modular e fácil
# de entender.

from __future__ import annotations
from abc import ABC, abstractmethod


class VendingMachine:
    def __init__(self) -> None:
        self.state: ProductState = InStock(self)

    def __str__(self) -> str:
        return f'Estado Atual: {self.state.__class__.__name__}'

    def buy_items(self):
        print('Tentando comprar o produto')
        print(f'Estado atual: {self.state.__class__.__name__}')
        self.state.buy()

    def add_to_stock(self):
        print('Tentando reabastecer produto.')
        print(f'Estado atual: {self.state.__class__.__name__}')
        self.state.refuel()

    def out_of_service(self):
        print('Tentando colocar o produto fora de serviço.')
        print(f'Estado atual: {self.state.__class__.__name__}')
        self.state.out_of_service()

    def in_service(self):
        print('Tentando reativar o serviço do produto.')
        print(f'Estado atual: {self.state.__class__.__name__}')
        self.state.on_service()


class ProductState(ABC):
    def __init__(self, machine: VendingMachine) -> None:
        self.machine = machine

    @abstractmethod
    def buy(self): pass

    @abstractmethod
    def refuel(self): pass

    @abstractmethod
    def out_of_service(self): pass

    @abstractmethod
    def on_service(self): pass


class InStock(ProductState):
    def buy(self):
        print('Produto em estoque, não irei comprar.')
        print(f'Estado não atualizado: {self.machine.state.__class__.__name__}')

    def refuel(self):
        self.machine.state = OutOfStock(self.machine)
        print('Produto foi reabastecido, agora está sem estoque')
        print(f'Estado atualizado: {self.machine.state.__class__.__name__}')

    def out_of_service(self):
        self.machine.state = OutOfService(self.machine)
        print('Produto fora de serviço.')
        print(f'Estado atualizado: {self.machine.state.__class__.__name__}')

    def on_service(self):
        print('Produto ja está em serviço.')
        print(f'Estado não atualizado: {self.machine.state.__class__.__name__}')


class OutOfStock(ProductState):
    def buy(self):
        self.machine.state = InStock(self.machine)
        print('Produto comprado e adicionado no estoque.')
        print(f'Estado atualizado: {self.machine.state.__class__.__name__}')

    def refuel(self):
        self.machine.state = OutOfStock(self.machine)
        print('Produto foi reabastecido, agora está sem estoque')
        print(f'Estado atualizado: {self.machine.state.__class__.__name__}')

    def out_of_service(self):
        self.machine.state = OutOfService(self.machine)
        print('Produto fora de serviço.')
        print(f'Estado atualizado: {self.machine.state.__class__.__name__}')

    def on_service(self):
        print('Produto ja está em serviço.')
        print(f'Estado não atualizado: {self.machine.state.__class__.__name__}')


class OutOfService(ProductState):
    def buy(self):
        print('Produto fora de serviço.')
        print(f'Estado não atualizado: {self.machine.state.__class__.__name__}')

    def refuel(self):
        print('Produto fora de serviço.')
        print(f'Estado não atualizado: {self.machine.state.__class__.__name__}')

    def out_of_service(self):
        print('Produto ja está fora de serviço.')
        print(f'Estado não atualizado: {self.machine.state.__class__.__name__}')

    def on_service(self):
        self.machine.state = OnService(self.machine)
        print(f'Estado atualizado: {self.machine.state.__class__.__name__}')


class OnService(ProductState):
    def buy(self):
        self.machine.state = InStock(self.machine)
        print('Produto comprado.')
        print(f'Estado atualizado: {self.machine.state.__class__.__name__}')

    def refuel(self):
        self.machine.state = OutOfStock(self.machine)
        print('Produto fora de estoque.')
        print(f'Estado atualizado: {self.machine.state.__class__.__name__}')

    def out_of_service(self):
        self.machine.state = OutOfService(self.machine)
        print('Produto sem serviço.')
        print(f'Estado atualizado: {self.machine.state.__class__.__name__}')

    def on_service(self):
        print('Produto ja está em serviço.')
        print(f'Estado não atualizado: {self.machine.state.__class__.__name__}')


if __name__ == '__main__':
    vm = VendingMachine()
    print(vm)

    vm.buy_items()
    print()
    vm.add_to_stock()
    print()
    vm.buy_items()
    print()
    vm.in_service()
    print()
    vm.out_of_service()
    print()
    vm.buy_items()
    print()
    vm.add_to_stock()
    print()
    vm.in_service()
    vm.buy_items()
