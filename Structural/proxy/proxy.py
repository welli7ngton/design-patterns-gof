"""
O proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
o proxy receberá as solicitarções e terá controle
sobre como e quanto repassar tais solicitações ao
objeto real.

com base no modo como os proxies são usados
nós os classificamos como:

- Proxy Virtual: controla acesso a recursos que podem ser caros para criação
ou utilização.
- Proxy Remoto: controlea acesso a recursos que estão em servidores remotos.
- Proxy de proteção: controla acesso a recursps que
possam necessitar autentificação ou permissão.
Proxy inteligente: além de controlar acesso ao objeto real, também executa
tarefas adicionais parasaber quando e como executar determinadas ações.

Proxies podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços. criar cache, criar e
destruir objetos, adiar execuções e muito mais...
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict
from time import sleep


class IUser(ABC):
    """ subject interface """
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> Dict: pass


class User(IUser):
    """ real subject """
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(2)
        return [
            {
                'rua': 'av brasil', 'numero': 345
            }
        ]

    def get_all_user_data(self) -> Dict:
        sleep(2)
        return {
            'cpf': '11111111111'
        }


class UserProxy(IUser):
    """ proxy """
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

        self._real_user: User
        self._cached_addresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = User(self.firstname, self.lastname)

    def get_addresses(self) -> List[Dict]:
        self.get_real_user()
        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()
        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


if __name__ == '__main__':
    wellington = UserProxy('wellington', 'almeida')

    print(wellington.firstname)
    print(wellington.lastname)

    print(wellington.get_all_user_data())
    print(wellington.get_addresses())

    print('CHACHED DATA:')
    for i in range(50):
        print(wellington.get_addresses())
