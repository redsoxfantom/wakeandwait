from wakeandwait.waiters.waiter import Waiter
from wakeandwait.waiters.waiter import WaiterException
from pythonping import ping

# ICMP protocol:
# https://en.wikipedia.org/wiki/Ping_(networking_utility)#ICMP_packet

class PingWaiter(Waiter):
    def __init__(self,**kwargs):
        if 'ip' not in kwargs:
            raise WaiterException("'ip' required when using Ping as a waiter")
        self.target_ip = kwargs['ip']
        self.timeout = 30
        if 'timeout' in kwargs:
            self.timeout = int(kwargs['timeout'])
        self.num_attempts = 2
        if 'num_attempts' in kwargs:
            self.num_attempts = int(kwargs['num_attempts'])
        self.packet_size = 1
        if 'packet_size' in kwargs:
            self.packet_size = int(kwargs['packet_size'])
        
    def wait(self):
        resplist = ping(self.target_ip,
                    verbose=True,
                    size=self.packet_size,
                    timeout=self.timeout,
                    count = self.num_attempts)
        success = False
        for resp in resplist:
            success |= resp.success
        return success