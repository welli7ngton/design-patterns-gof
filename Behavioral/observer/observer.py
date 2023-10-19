"""
O padrão Observer tem a intenção de definir uma dependência de um-para-muitos
entre objetos, de maneira que quando um objeto muda de estado, todo os seus
dependentes são notificados e atulaizados automaticamente.

Um observer é um objeto que gostaria de ser informado, um observable(subject)
é a entidade que gera as informações.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObservable(ABC):
    @property
    @abstractmethod
    def state(self): pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observers(self) -> None: pass


class WheatherStation(IObservable):
    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: Dict):
        new_state: Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state: Dict = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class Smartphone(IObserver):
    def __init__(self, name: str, observable: IObservable) -> None:
        self.name = name
        self._observable = observable

    def update(self) -> None:
        obs_name = self._observable.__class__.__name__
        print(
            f'{self.name} o objeto {obs_name}'
            f'acabou de ser atualizado -> {self._observable.state}'
        )
        print()


if __name__ == '__main__':
    ws = WheatherStation()
    smarthpone = Smartphone('Iphone', ws)
    s2 = Smartphone('Galaxy', ws)
    ws.add_observer(smarthpone)
    ws.add_observer(s2)

    ws.state = {'temp': '30'}
    ws.state = {'clima': 'nublado'}
    ws.state = {'temp': '40'}

    ws.remove_observer(s2)
    ws.reset_state()
