"""
Chain of responsibility(COR) é um padrão comportamental que tema  aintenção de
evitar o acoplamento do remetende de uma solicitação ao seu receptor. ao dar
a mais de um objeto a oportunidade de tratar a solicitação. encadear os
objetos receptores repassando a solicitação ao longo da cadeia até que um
objeto a trate.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handle(self): pass


class HanderABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.sucessor = sucessor
        self.letters = ['A', 'B', 'C']

    def handle(self, letter: str):
        if letter in self.letters:
            return f"HanderABC: consegui resolver a letra {letter}"
        return self.sucessor.handle(letter)


class HanderDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.sucessor = sucessor
        self.letters = ['D', 'E', 'F']

    def handle(self, letter: str):
        if letter in self.letters:
            return f"HanderDEF: consegui resolver a letra {letter}"
        return self.sucessor.handle(letter)


class HandlerUnsolved(Handler):
    def handle(self, letter: str):
        return f"HandlerUnsolved: não consegui resolver a letra {letter}"


if __name__ == '__main__':
    handler_unsolved = HandlerUnsolved()
    handler_def = HanderDEF(handler_unsolved)
    handler_abc = HanderABC(handler_def)

    print(handler_abc.handle('A'))
    print(handler_abc.handle('B'))
    print(handler_abc.handle('C'))
    print(handler_abc.handle('D'))
    print(handler_abc.handle('E'))
    print(handler_abc.handle('F'))
    print(handler_abc.handle('G'))
    print(handler_abc.handle('H'))
    print(handler_abc.handle('I'))
    print()
    print(handler_def.handle('A'))
    print(handler_def.handle('B'))
    print(handler_def.handle('C'))
    print(handler_def.handle('D'))
    print(handler_def.handle('E'))
    print(handler_def.handle('F'))
    print(handler_def.handle('G'))
    print(handler_def.handle('H'))
    print(handler_def.handle('I'))
    print()
    print(handler_unsolved.handle('A'))
    print(handler_unsolved.handle('B'))
    print(handler_unsolved.handle('C'))
    print(handler_unsolved.handle('D'))
    print(handler_unsolved.handle('E'))
    print(handler_unsolved.handle('F'))
    print(handler_unsolved.handle('G'))
    print(handler_unsolved.handle('H'))
    print(handler_unsolved.handle('I'))
