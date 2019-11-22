from wakeandwait.waiters.ping import Ping
from wakeandwait.waiters.waiter import Waiter
from wakeandwait.waiters.waiter import WaiterException

def waiter_factory(waiter_type: str, **kwargs) -> Waiter:
    if waiter_type.lower() == 'ping':
        inst = Ping(**kwargs)
        return inst
    raise WaiterException(F"Waiter Type {waiter_type} not supported")
