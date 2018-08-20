from log import logger
import time


class FakeRobot:
    def __init__(self):
        self.storage = []
        self.count = 0

    def reset(self):
        del self.storage[:]

    def transfer(self, func):
        logger.info('transfer start')

        def collect(*args, **kwargs):
            if kwargs.get('content', None) is None:
                self.storage.append([args[0].text, args[0].sender.name])
                return func(*args, **kwargs)
        return collect

    def spawn(self):
        while True:
            logger.info(self.storage)
            time.sleep(0.5)
            if len(self.storage) > 0:
                break
        info = self.storage[0]
        del self.storage[0]
        return info





