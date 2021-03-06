import time
from datetime import datetime


class KeepIt100(object):
    def __init__(self, shared):
        self.shared = shared

    def collect(self):
        data = {
            'time': datetime.now().isoformat(),
            'name': 'mock.keepit100',
            'value': 100
        }
        time.sleep(1)
        return data
