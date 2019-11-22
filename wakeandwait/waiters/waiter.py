class Waiter(object):
    def wait(self, timeout):
        raise NotImplementedError

class WaiterException(Exception):
    pass