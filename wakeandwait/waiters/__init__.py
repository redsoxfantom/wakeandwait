from wakeandwait import ParseableEnum

class WaiterType(ParseableEnum):
    PING = "ping"

def waiter_factory(waiter_type):
    pass