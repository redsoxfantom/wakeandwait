from wakeandwait.wakers.waker import Waker
from wakeandwait.wakers.waker import NullWaker
from wakeandwait.wakers.waker import WakerException
from wakeandwait.wakers.wol import WolWaker

def waker_factory(waker_type: str, **kwargs) -> Waker:
    if waker_type == None or waker_type.lower() == 'null':
        return NullWaker()
    if waker_type.lower() == "wol" or waker_type.lower() == "wakeonlan":
        return WolWaker(**kwargs)
    raise WakerException(F"Waker type {waker_type} not supported")