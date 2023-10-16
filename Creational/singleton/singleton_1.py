"""
O Singleton tem a intenção de garantir que uma classe tenha somente uma
instância e fornece um ponto global de acesso para a mesma.
"""


class AppSettings:
    _instace = None

    def __new__(cls, *args, **kwargs):
        if not cls._instace:
            cls._instace = super().__new__(cls, *args, **kwargs)
        return cls._instace

    def __init__(self) -> None:
        # o init será chamado todas as vezes que a classe for instanciada
        # causando um problema no singleton.
        self.theme = 'dark'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.theme = 'light'
    print(as1.theme)

    as2 = AppSettings()
    print(as1.theme)
