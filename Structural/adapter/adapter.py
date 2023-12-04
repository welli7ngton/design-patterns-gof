"""
Adapter é um padrão de projeto estrutural que
tem a intenção de permitir que duas classes
que seriam incompatíveis trabalharem em conjunto
através de um "adaptador."
"""

from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self): pass

    @abstractmethod
    def right(self): pass

    @abstractmethod
    def down(self): pass

    @abstractmethod
    def left(self): pass


class Control(IControl):
    def top(self):
        print("Movendo para cima")

    def right(self):
        print("Movendo para direita")

    def down(self):
        print("Movendo para baixo")

    def left(self):
        print("Movendo para esquerda")


class NewControl:
    def move_top(self):
        print("Movendo para cima")

    def move_right(self):
        print("Movendo para direita")

    def move_down(self):
        print("Movendo para baixo")

    def move_left(self):
        print("Movendo para esquerda")


class ControlAdapter:
    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self):
        self.new_control.move_top()

    def right(self):
        self.new_control.move_right()

    def down(self):
        self.new_control.move_down()

    def left(self):
        self.new_control.move_left()


if __name__ == '__main__':
    new_control = NewControl()

    c1 = ControlAdapter(new_control)
    c1.top()
    c1.right()
    c1.down()
    c1.left()
