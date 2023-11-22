from __future__ import annotations
from typing import List, Dict
from abc import ABC, abstractmethod


class IObervable(ABC):
    @property
    @abstractmethod
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

    @abstractmethod
    def subscribe(self, channel: IObervable): pass

    @abstractmethod
    def unsubscribe(self, channel: IObervable): pass


class Notification:
    @classmethod
    def notification(cls, channel: str, title: str, type: str, duration: str):
        return {
            'Title': title,
            'Channel': channel,
            'Type': type,
            'Duration': duration,
        }


# in theses classes we have an many-to-many relationship using the Youtube
# notification logic.
class YoutubeChannel(IObervable):
    def __init__(self, channel_name: str) -> None:
        self.channel_name = channel_name
        self._subscribers: List[IObserver] = []
        self._state: Notification

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state: Notification):
        self._state = new_state
        self.notify_observers()

    def add_observer(self, observer: IObserver):
        self._subscribers.append(observer)

    def remove_observer(self, observer: IObserver):
        if observer not in self._subscribers:
            return
        self._subscribers.remove(observer)

    def notify_observers(self):
        for subscriber in self._subscribers:
            subscriber.update(self.channel_name)


class YoutubeUser(IObserver):
    def __init__(self, name) -> None:
        self.name = name
        self._channels_subscription: Dict = {}

    def update(self, channel_key: str):
        print(self.name)
        print(self._channels_subscription[channel_key]._state, '\n')

    def subscribe(self, channel: IObervable):
        self._channels_subscription[channel.channel_name] = channel
        channel.add_observer(self)

    def unsubscribe(self, channel: IObervable):
        self._channels_subscription.pop(channel.channel_name)
        channel.remove_observer(self)
        print(f'You have unsubscribed {channel.channel_name}\n')


if __name__ == '__main__':
    # creating a Youtube Channel
    mr_beast = YoutubeChannel('Mr Beast')
    frttt = YoutubeChannel('FRTT')

    # creating a Youtube User
    user1 = YoutubeUser('Wellington')
    user2 = YoutubeUser('Almeida')
    user3 = YoutubeUser('Silva')

    # subscribe process
    user1.subscribe(mr_beast)
    user2.subscribe(mr_beast)
    user3.subscribe(mr_beast)

    user1.subscribe(frttt)

    mr_beast.state = Notification.notification(
        mr_beast.channel_name,
        'New Video',
        'Funny video',
        '20:53',
    )

    user1.unsubscribe(mr_beast)

    frttt.state = Notification.notification(
        frttt.channel_name,
        'Analise!',
        'Valorant Content',
        '15:00',
    )
