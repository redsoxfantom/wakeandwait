class Waker(object):
    def wake(self):
        raise NotImplementedError

class NullWaker(Waker):
    def wake(self):
        return True

class WakerException(Exception):
    pass