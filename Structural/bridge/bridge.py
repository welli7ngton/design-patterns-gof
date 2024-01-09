"""
Bridge é um padrão de projeto estrutural que
tem a intenção de desacoplar uma abstração
da sua implementação, de modo que as duas
possam variar e evoluir independentemente.

Abstração é uma camada de alto npível para algo.
Geralmente, a abstração não faz nenhum trabalho
por conta própria, ela delega parte ou todo o
trabalho para a camada de implementação.

RELEMBRANDO: Adapter é um padrão de projeto
estrutural que tem a intenção de permitir
que duas classes que seriam incompatíveis
trabalharem em conjunto através de um "adaptador".

Diferença(GOF) - A diferença chave
entre esses padrões está nas suas intenções...
O padrão Adapter faz as coisas funcionarem
APÓS els terem sido projetadas; o Bridge as
faz funcionar ANTES QUE existam.
"""


from __future__ import annotations
from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self) -> None: pass

    @abstractmethod
    def decrease_volume(self) -> None: pass

    @abstractmethod
    def power(self) -> None: pass


class RemoteControl(IRemoteControl):
    def __init__(self, device: IDevice) -> None:
        self._device = device

    def increase_volume(self) -> None:
        self._device.volume += 10

    def decrease_volume(self) -> None:
        self._device.volume -= 10

    def power(self) -> None:
        self._device.power = not self._device.power


class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self) -> int: pass

    @volume.setter
    def volume(self, volume: int) -> None: pass

    @property
    @abstractmethod
    def power(self) -> bool: pass

    @power.setter
    def power(self, power: bool) -> None: pass


class TV(IDevice):
    def __init__(self) -> None:
        self._volume = 10
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        if not self.power:
            print(f'Please, turn {self._name} ON.')
            return

        if volume > 100:
            print('Max volume reached.')
            return

        if volume < 0:
            print('Min volume reached.')
            return

        self._volume = volume
        print(f'Volume is now {self._volume}.')

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool) -> None:
        self._power = power
        power_status = 'ON' if self.power else 'OFF'
        print(f'{self._name} is Now {power_status}.')


class Radio(TV):
    ...


if __name__ == '__main__':
    tv = TV()
    radio = Radio()

    remote = RemoteControl(tv)

    print('TV:')
    remote.increase_volume()
    remote.power()

    # increasing the volume
    for i in range(10):
        remote.increase_volume()

    remote.power()

    remote.power()
    # decreasing the volume
    for j in range(11):
        remote.decrease_volume()

    print()
    print('Radio:')
    remote = RemoteControl(radio)

    remote.increase_volume()
    remote.power()

    # increasing the volume
    for i in range(10):
        remote.increase_volume()

    remote.power()

    remote.power()
    # decreasing the volume
    for j in range(11):
        remote.decrease_volume()
