from wakeandwait.waiters import waiter_factory
from wakeandwait.wakers import waker_factory

def wakeandwait(waker,waiter,**kwargs):
    waker = waker_factory(waker,**kwargs)
    waiter = waiter_factory(waiter,**kwargs)
    print(F"Running wakeandwait with waker {waker} and waiter {waiter}")
    if not waker.wake():
        print("Waker failed")
        return False
    if not waiter.wait():
        print("Waiter failed")
        return False
    return True