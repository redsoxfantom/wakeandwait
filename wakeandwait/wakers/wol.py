from wakeandwait.wakers.waker import Waker
from wakeandwait.wakers.waker import WakerException
from wakeonlan import send_magic_packet

class WolWaker(Waker):
    def __init__(self,**kwargs):
        if 'mac' not in kwargs:
            raise WakerException("'mac' required when using WakeOnLan as waker")
        self.mac = kwargs['mac']

    def wake(self):
        send_magic_packet(self.mac)
        return True