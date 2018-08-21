from log import logger
import time


class FakeRobot:
    def __init__(self):
        self.register_list = {}
        self.storage = {}
        self.count = 0

    def end_activity(self, puid):
        self.register_list[puid] = None
        del self.storage[puid][:]        

    def register_activity(self, puid, activity):
        if self.register_list.get(puid, None) is None:
            self.register_list[puid] = activity
            self.storage[puid] = []
            return True
        return False

    def transfer(self, func):
        logger.info('transfer start')

        def collect(*args, **kwargs):
            if self.register_list.get(args[0].sender.puid, None) is not None:
                self.storage[args[0].sender.puid].append([args[0].text, args[0].sender.name])
            return func(*args, **kwargs)
        return collect

    def spawn(self, puid):
        t1 = time.time()
        while True:
            time.sleep(1)
            if len(self.storage[puid]) > 0:
                break
            if time.time()-t1>5:
                return [None, None]
        info = self.storage[puid][0]
        del self.storage[puid][0]
        return info





