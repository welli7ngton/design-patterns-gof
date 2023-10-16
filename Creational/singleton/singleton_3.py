"""
class Meta(type):
    def __call__(self, *args, **kwargs):
        print('CALL da metaclass é executado')
        return super().__call__(*args, **kwargs)


class Person(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('NEW é executado')
        return super().__new__(cls)

    def __init__(self, nome):
        print('INIT é executado')
        self.nome = nome

    def __call__(self, x, y):
        print('Call chamado', self.nome, x + y)


if __name__ == '__main__':
    p1 = Person('Wellington')
    p1(1, 2)

Explicação da ordem de execução dos métodos especiais
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        self.theme = 'dark'


if __name__ == '__main__':
    # a partir de agora qualquer instancia da classe AppSettings referencia
    # o mesmo objeto
    as1 = AppSettings()
    as1.theme = 'light'
    print(as1.theme)

    as2 = AppSettings()
    print(as1.theme, 'as1')
    print(as2.theme, 'as2')

    print(as1 == as2)
