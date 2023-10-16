"""
Monostate(ou Borg) - É uma variação do Singleton proposto por Alex Martelli que
tem a intenção de garntir que o estado do objeto seja igual para todas as
instâncias.
"""


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    _state = {}

    def __init__(self, nome=None, sobrenome=None) -> None:
        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == '__main__':
    m1 = MonoStateSimple(nome='Wellington')
    m2 = MonoStateSimple(sobrenome='Almeida')

    print(m1)
    print(m2)
