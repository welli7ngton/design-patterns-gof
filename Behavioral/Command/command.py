"""
Com o padrão de projeto Command, você pode encapsular uma solicitação como um
objeto, permitindo que você parametrize clientes com diferentes solicitações
enfileire ou registre solicitações e suporte operações que podem ser desfeitas.

Imagine que você esteja desenvolvendo uma aplicação de edição de texto e queira
permitir que o usuário desfaça e refaça suas ações. O padrão de projeto Command
pode ser usado para implementar essa funcionalidade.

A ideia básica é encapsular cada ação do usuário como um objeto Command, que
armazena informações sobre a ação e fornece um método para executá-la e outro
para desfazê-la. Esses objetos Command são então enfileirados ou registrados em
um objeto invocador, que é responsável por executá-los e desfazê-los.
"""

if __name__ == '__main__':
    pass
