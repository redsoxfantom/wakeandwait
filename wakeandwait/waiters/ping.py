import struct
from random import randrange
import socket
import sys
from wakeandwait.waiters.waiter import Waiter
from wakeandwait.waiters.waiter import WaiterException

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
        self.my_id = randrange(start=0,stop=65535)
        self.packet_size = 32
        if 'packet_size' in kwargs:
            self.packet_size = int(kwargs['packet_size'])
        try:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.getprotobyname('icmp'))
        except Exception as ex:
            if ex.errno == 1: # Permission denied
                raise Exception("You must be root to use Ping")
            else:
                raise
        
    def wait(self):
        seq_num = 0
        icmp_echo_reply = 0

    def _create_packet(self,seq_num):
        icmp_echo = 8
        checksum = 0

        header = struct.pack(
            "!BBHHH", icmp_echo, 0, checksum, self.my_id, seq_num
        )
