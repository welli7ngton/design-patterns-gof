"""
Memento é um padrão de projeto comportamental
que tema a intenção de permitir que você salve e restaure
um estado anterios de um objeto originator sem revelar os
detalhes da sua implementação e sem violar o encapsulamento.

Originator é o objeto que deseja salvar seu estado.
Memento é usado para salvar o estado do Originator.
Caretaker é usado para armazenar mementos.
Caretaker também é usado com o Padrão Command.
"""


from __future__ import annotations
from typing import Any, Dict, List
from copy import deepcopy


class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        super().__setattr__('_state', state)

    def get_state(self):
        return self._state

    def __setattr__(self, __name: str, __value: Any) -> None:
        raise AttributeError('Im immutable.')


class ImageEditor:
    def __init__(self, name: str, width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.heigth = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'


class Caretaker:
    def __init__(self, originator: ImageEditor) -> None:
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        if not self._mementos:
            return
        self._originator.restore(self._mementos.pop())


if __name__ == '__main__':
    img = ImageEditor('foto_1.svg', 111, 111)
    caretaker = Caretaker(img)

    img.name = 'foto_2.svg'
    img.width = 222
    img.heigth = 222
    caretaker.backup()

    img.name = 'foto_3.svg'
    img.width = 333
    img.heigth = 333
    caretaker.backup()

    img.name = 'foto_4.svg'
    img.width = 444
    img.heigth = 444
    caretaker.backup()

    caretaker.restore()
    print(img)
    caretaker.restore()
    print(img)
    caretaker.restore()
    print(img)
    caretaker.restore()
    print(img)
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    print(img)
