from wakeandwait.waiters.waiter import Waiter
from wakeandwait.waiters.waiter import WaiterException

class Ping(Waiter):
    def __init__(self,**kwargs):
        if 'ip' not in kwargs:
            raise WaiterException("'ip' required when using Ping as a waiter")
        self.target_ip = kwargs['ip']

    def wait(self,timeout):
        pass