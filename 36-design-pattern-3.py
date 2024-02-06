### Observer

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


class Subscriber(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, video_title):
        print(f"Hey {self.name}, a new video is uploaded: {video_title}")


class YoutubeChannel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, video_title):
        for subscriber in self.subscribers:
            subscriber.update(video_title)

    def upload_video(self, video_title):
        self.notify(video_title)


channel = YoutubeChannel()
subscriber1 = Subscriber("Alice")
subscriber2 = Subscriber("Bob")

channel.subscribe(subscriber1)
channel.subscribe(subscriber2)

channel.upload_video("Python Design Patterns")
print('----')

channel.unsubscribe(subscriber2)
channel.upload_video("Python OOP")
