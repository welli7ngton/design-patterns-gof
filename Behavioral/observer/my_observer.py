from abc import ABC, abstractmethod


class IObervable(ABC):
    @property
    def state(self): pass

    @abstractmethod
    def add_observer(self): pass

    @abstractmethod
    def remove_observer(self): pass

    @abstractmethod
    def notify_observers(self): pass


class IObserver(ABC):
    @abstractmethod
    def update(self): pass


class Notification:
    def __init__(self, title, type, duration) -> None:
        self.title = title
        self.type = type
        self.duration = duration


class ContentCreator(IObervable):
    def __init__(self, name) -> None:
        self.name = name
        self._observers = {}
        self._state: Notification | None = None

    def add_observer(self, observer: IObserver):
        self._observers[observer.nickname] = observer

    def remove_observer(self, observer):
        if observer.nickname in self._observers:
            self._observers.pop(observer.nickname)

    def notify_observers(self):
        for observer in self._observers.values():
            observer.update()

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_notification: Notification):
        self._state = new_notification
        self.notify_observers()


class Subscriber(IObserver):
    def __init__(self, nickname, observable: IObervable) -> None:
        self.nickname = nickname
        self.observable = observable

    def update(self):
        print(self.nickname)
        print(f'New video: {self.observable._state.title}')
        print(f'Type: {self.observable._state.type}')
        print(f'Creator: {self.observable.name}')
        print(f'Duration: {self.observable._state.duration}')
        print()


if __name__ == '__main__':
    # create a observable(content creator)
    elon_musk = ContentCreator('Elon Musk')

    # create users wich follow Elon Musk
    user1 = Subscriber('wellington', elon_musk)
    user2 = Subscriber('Jose', elon_musk)
    user3 = Subscriber('Maria', elon_musk)

    # content creator(Observable) add his Observers
    elon_musk.add_observer(user1)
    elon_musk.add_observer(user2)
    elon_musk.add_observer(user3)

    # Elon Musk sent the notification(change his state) to all his subscribers
    elon_musk.state = Notification('New Tesla', 'Cars', '18:00')

    # all the updates are made in the users

    elon_musk.remove_observer(user1)

    elon_musk.state = Notification('New X update', 'Social media', '45:00')
