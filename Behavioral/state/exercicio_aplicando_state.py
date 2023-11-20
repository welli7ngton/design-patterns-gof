# Exercício de Refatoração usando o Padrão State

# Você foi designado para refatorar um sistema de controle de luz que
# atualmente possui uma implementação simples sem o uso do padrão State.
# A classe Luz atual tem métodos para ligar e desligar, mas à medida que
# o sistema cresce, torna-se evidente que novos estados e comportamentos
# relacionados ao estado podem ser adicionados.

# Sua tarefa é aplicar o padrão State para tornar o sistema mais flexível
# e extensível. Aqui estão as etapas sugeridas:

# Crie uma interface EstadoLuz que declare métodos para cada ação que a
# luz pode realizar, como ligar e desligar.Implemente classes concretas
# que implementem essa interface para representar os diferentes estados
# da luz, por exemplo, LuzLigada e LuzDesligada.Modifique a classe Luz
# para ter uma referência para um objeto de estado atual, inicializado
# com o estado padrão (LuzDesligada, por exemplo).Atualize os métodos
# da classe Luz para delegar as chamadas de método para o objeto de
# estado atual.

from __future__ import annotations
from abc import ABC, abstractmethod


class LightState(ABC):
    def __init__(self, light: Light) -> None:
        self.light = light

    @abstractmethod
    def open(self): pass

    @abstractmethod
    def close(self): pass


class LightOpen(LightState):
    def open(self):
        print('A luz já está ligada.')

    def close(self):
        print('A luz foi desligada.')
        self.light.state = LightClose(self.light)


class LightClose(LightState):
    def open(self):
        print('A luz foi ligada.')
        self.light.state = LightOpen(self.light)

    def close(self):
        print('A luz já está desligada.')


class Light:
    def __init__(self) -> None:
        self.state = LightClose(self)

    def light_open(self):
        self.state.open()

    def light_close(self):
        self.state.close()


if __name__ == '__main__':
    luz = Light()
    luz.light_close()
    luz.light_open()
    luz.light_open()
