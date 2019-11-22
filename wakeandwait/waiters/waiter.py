class Waiter(object):
    def wait(self):
        raise NotImplementedError

class WaiterException(Exception):
    pass