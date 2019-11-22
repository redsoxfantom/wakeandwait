from wakeandwait.waiters import waiter_factory

def wakeandwait(waker,waiter,**kwargs):
    waiter = waiter_factory(waiter,**kwargs)