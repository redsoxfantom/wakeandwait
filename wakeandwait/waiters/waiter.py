class Waiter(object):
    def wait(self):
        raise NotImplementedError

class NullWaiter(Waiter):
    def wait(self):
        return True

class WaiterException(Exception):
    pass