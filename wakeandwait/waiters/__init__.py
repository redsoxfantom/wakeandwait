from wakeandwait.waiters.ping import Ping
from wakeandwait.waiters.waiter import Waiter
from wakeandwait.waiters.waiter import WaiterException
from wakeandwait.waiters.waiter import NullWaiter

def waiter_factory(waiter_type: str, **kwargs) -> Waiter:
    if waiter_type == None or waiter_type.lower() == 'null':
        return NullWaiter()
    if waiter_type.lower() == 'ping':
        return Ping(**kwargs)
    raise WaiterException(F"Waiter Type {waiter_type} not supported")
