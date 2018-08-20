from log import logger

class FakeRobot:
    def __init__(self):
        self.storge = []
        self.count = 0

    def reset(self):
        del self.storge[:]

    def transfer(self, func):
        logger.info('transfer start')
        def collect(*args, **kwargs):
            if kwargs.get('content',None) is None:
                self.storge.append([args[0].text, args[0].sender.name])
                return func(*args, **kwargs)
        return collect

    def spawn(self):
        if len(self.storge)>0 :
            info = self.storge[0]
            del self.storge[0]
            return info
        return ['','']





