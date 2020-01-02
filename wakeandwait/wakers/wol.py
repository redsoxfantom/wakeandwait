from wakeandwait.wakers.waker import Waker
from wakeandwait.wakers.waker import WakerException

class WolWaker(Waker):
    def __init__(self,**kwargs):
        pass

    def wake(self):
        return True