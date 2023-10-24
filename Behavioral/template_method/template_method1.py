"""
Template Metohd(comportamental) tem a intenção de definir um algoritmo em um
método, posterfando alguns passos para as subclasses por herança. Template
method permite que subclasses redefinam certos passos de um algoritmo sem
mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses utilizem caso
necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC) - Inversão de controle
"""
from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.operation1()
        self.operation2()

    @abstractmethod
    def operation1(self): pass

    @abstractmethod
    def operation2(self): pass


class Concrete1(Abstract):
    def operation1(self):
        print('Operation 1')

    def operation2(self):
        print('Operation 2')


class Concrete2(Abstract):
    def operation1(self):
        print('Operation 1(diferente)')

    def operation2(self):
        print('Operation 2(diferente)')


if __name__ == '__main__':
    c1 = Concrete1()
    c1.template_method()

    c2 = Concrete2()
    c2.template_method()
