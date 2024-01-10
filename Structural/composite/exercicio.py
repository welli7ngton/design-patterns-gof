"""
Você foi designado para desenvolver um sistema de representação hierárquica de
estruturas organizacionais. Cada elemento da estrutura pode ser tanto um
indivíduo quanto uma equipe, e cada equipe pode conter indivíduos e outras
equipes. O objetivo é criar uma estrutura que permita realizar operações como
a obtenção do custo total da organização, a exibição da hierarquia de forma
hierárquica e a adição/remoção de elementos dinamicamente.

Utilize o padrão de projeto Composite para implementar essa estrutura.
Certifique-se de que sua solução permita a manipulação eficiente de elementos
individuais e de grupos, bem como a capacidade de compor estruturas complexas.
Ao criar as classes, considere também a possibilidade de estender a hierarquia
no futuro, adicionando novos tipos de elementos.

Lembre-se de que o objetivo é utilizar o padrão de projeto Composite de
maneira eficiente e elegante, encapsulando a complexidade da hierarquia
de elementos em classes bem estruturadas. Ao concluir a implementação, forneça
exemplos de uso que destaquem as capacidades da estrutura hierárquica criada.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class EquipStructure(ABC):
    @abstractmethod
    def get_total_cust(self) -> float: pass

    @abstractmethod
    def show_equip(self) -> None: pass

    def add(self, member: EquipStructure) -> None: pass

    def remove(self, member: EquipStructure) -> None: pass


class Equip(EquipStructure):
    def __init__(self, equip_name: str) -> None:
        self.equip_name = equip_name
        self._members = []

    def get_total_cust(self) -> float:
        return sum([
            member.get_total_cust() for member in self._members
        ])

    def show_equip(self) -> None:
        print(f'\n{self.equip_name}')
        for member in self._members:
            member.show_equip()

    def add(self, member: EquipStructure) -> None:
        self._members.append(member)

    def remove(self, member: EquipStructure) -> None:
        if member in self._members:
            self._members.remove(member)


class Member(EquipStructure):
    def __init__(self, name: str, cust: float) -> None:
        self.name = name
        self.cust = cust

    def get_total_cust(self) -> float:
        return self.cust

    def show_equip(self) -> None:
        print(self.name)

    def add(self, member: EquipStructure) -> None:
        pass

    def remove(self, member: EquipStructure) -> None:
        pass


if __name__ == '__main__':
    wellington = Member('wellington', 1000.00)
    marilia = Member('marilia', 1000.00)
    jorge = Member('jorge', 1000.00)

    equip1 = Equip('Equipe 1')
    equip1.add(wellington)
    equip1.add(marilia)
    equip1.add(jorge)

    tosco = Member('tosco', 500.00)
    aparecida = Member('aparecida', 500.00)
    pitito = Member('pitito', 500.00)
    luke = Member('luke', 500.00)

    equip2 = Equip('Equipe 2')
    equip2.add(tosco)
    equip2.add(aparecida)
    equip2.add(pitito)
    equip2.add(luke)

    jeguelson = Member('jeguelson', 2000.00)

    equip3 = Equip('Equipe 3')
    equip3.add(jeguelson)

    team = Equip('Time Geral')
    team.add(equip1)
    team.add(equip2)
    team.add(equip3)
    team.show_equip()
    print(team.get_total_cust())

    team2 = Equip('Time 2')
    team2.add(equip1)
    team2.add(equip2)

    team2.show_equip()
    print(team2.get_total_cust())
