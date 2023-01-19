from util.publisher_subscriber.ISubscriber import ISubscriber


class MockSubscriber(ISubscriber):

    def __init__(self):
        self.has_been_notified = False

    def is_notified(self) -> bool:
        return self.has_been_notified

    def notify(self):
        self.has_been_notified = True
