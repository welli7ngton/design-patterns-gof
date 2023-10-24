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
from __future__ import annotations
from abc import ABC, abstractmethod


class Light:
    # Receiver

    def __init__(self, name: str, room: str) -> None:
        self.name = name
        self.room = room
        self.color = 'White'
        self.state = False

    def turn_light_on(self):
        self.state = True
        print(f'{self.name} in {self.room} is now ON.')

    def turn_light_off(self):
        self.state = False
        print(f'{self.name} in {self.room} is now OFF.')

    def change_color(self, new_color: str):
        if self.state:
            self.color = new_color
            print(f'{self.name} in {self.room} is now {self.color}.')
            return
        print('cant change the color with the light turned off.')


class ICommand(ABC):
    # command interface
    @abstractmethod
    def execute(self): pass

    @abstractmethod
    def undo(self): pass


class TurnLightOn(ICommand):
    # concrete command initializing with the receiver
    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self):
        if self.light.state:
            print(f'{self.light.name} is already on.')
            return
        self.light.turn_light_on()

    def undo(self):
        if not self.light.state:
            print(f'{self.light.name} is already off.')
            return
        self.light.turn_light_off()


class ChangeColor(ICommand):
    def __init__(self, light: Light, new_color: str) -> None:
        self.light = light
        self.new_color = new_color
        self._old_color = light.color

    def execute(self):
        self._old_color = self.light.color
        self.light.change_color(self.new_color)

    def undo(self):
        self.light.change_color(self._old_color)


class Invoker:
    # invoker have an many-to-one relationship with command
    def __init__(self) -> None:
        self._commands = {}

    def add_command(self, command_name: str, command: ICommand):
        self._commands[command_name] = command

    def activate_command(self, command_name):
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
            return
        print('command not found.')

    def deactivate_command(self, command_name):
        if command_name in self._commands.keys():
            self._commands[command_name].undo()
            return
        print('command not found.')


if __name__ == '__main__':
    # creating receiver object :: receiver
    bedroom_l1 = Light('Light 1', 'Bedroom')
    bedroom_l2 = Light('Light 2', 'Bedroom')

    # creating a concrete command :: command -> receiver
    concrete_command_1 = TurnLightOn(bedroom_l1)
    concrete_command_2 = TurnLightOn(bedroom_l2)
    concrete_command_3 = ChangeColor(bedroom_l1, 'Red')
    concrete_command_4 = ChangeColor(bedroom_l2, 'Blue')
    concrete_command_5 = ChangeColor(bedroom_l1, 'Purple')

    # creating a invoker
    invoker = Invoker()

    # setting up a invoker with commands :: invoker -> command -> receiver
    invoker.add_command('light_1', concrete_command_1)
    invoker.add_command('light_2', concrete_command_2)
    invoker.add_command('change_color_1', concrete_command_3)
    invoker.add_command('change_color_2', concrete_command_4)
    invoker.add_command('change_color_1_2', concrete_command_5)

    invoker.activate_command('light_1')
    invoker.activate_command('light_2')

    invoker.activate_command('change_color_1')
    invoker.activate_command('change_color_1_2')
    invoker.deactivate_command('change_color_1')
