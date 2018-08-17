
class FakeRobot:
    def __init__(self):
        self.count = 0

    def spawn(self):
        arr = ['如意金箍棒', '诸葛亮', '林黛玉']
        self.count += 1
        return arr[self.count % len(arr)], 'sunfei'





