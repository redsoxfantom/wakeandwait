from enum import Enum

class ParseableEnum(Enum):
    @classmethod
    def parse_value(cls,value):
        for enum_val in list(cls):
            if enum_val.value.lower() == value.lower():
                return enum_val
        return None

def wakeandwait(waker,macAddr,waiter,ipaddress):
    pass