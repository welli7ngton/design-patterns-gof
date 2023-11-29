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
from typing import Dict, List
from copy import deepcopy


class Memento:
    def __init__(self) -> None:
        pass


if __name__ == '__main__':
    pass
