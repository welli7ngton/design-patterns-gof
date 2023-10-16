"""
Builder é um padrão de criação que tem a intenção de separar a construção de um
objeto complexo de sua representação, de modo que o mesmo processo de
construção possa criar diferentes represetações.

Builder te da a possibilidade de criar objetos passo-apasso e isso já é
possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos(method chaining).
"""
from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class User(StringReprMixin):
    def __init__(self) -> None:
        self.first_name = None
        self.last_name = None
        self.age = None
        self.phone = []
        self.addresses = []


# interface abstrata do Builder
class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_first_name(self, first_name): pass

    @abstractmethod
    def add_last_name(self, last_name): pass

    @abstractmethod
    def add_age(self, age): pass

    @abstractmethod
    def add_phone(self, phone): pass

    @abstractmethod
    def add_addresses(self, address): pass


class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_first_name(self, first_name):
        self._result.first_name = first_name
        return self

    def add_last_name(self, last_name):
        self._result.last_name = last_name
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    def add_phone(self, phone):
        self._result.phone.append(phone)
        return self

    def add_addresses(self, address):
        self._result.addresses.append(address)
        return self


class UserDirector:
    def __init__(self, builder: UserBuilder):
        self._builder = builder

    def with_age(self, first_name, last_name, age):
        self._builder.add_first_name(first_name)\
            .add_last_name(last_name).add_age(age)
        return self._builder.result

    def with_address(self, first_name, last_name, address):
        self._builder.add_first_name(first_name)\
            .add_last_name(last_name).add_addresses(address)
        return self._builder.result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)

    user1 = user_director.with_age('wellington', 'almeida', 20)
    user2 = user_director.with_address('maria', 'miranda', 'avenida brasil')

    print(user1)
    print(user2)
