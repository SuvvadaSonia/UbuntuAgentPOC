"""
    It makes the SSH connection from client's device to client's network device
"""
from pprint import pprint
from typing import NewType, Any, Tuple
import paramiko

class SSHAgent:
    __HOST = NewType('host',Any)
    __USER = NewType('user',Any)
    __PWD = NewType('password', Any)

    def __init__(self,jumpDevice:Tuple[str,str,str],remoteDevice:Tuple[str,str,str]):
    # def __init__(self,jumpDevice:tuple,remoteDevice:tuple):
        """
        First, It will enable SSH connection To Jump Device over VPN from main server.
        And after, It will establish the SSH connection from Jump Device to End Device.

        @param tuple jumpDevice: Middle device host & credenatil details
        @param tuple remoteDevice: End device credentials
        """
        __jump_host, __jump_user, __jump_pwd = jumpDevice
        __remote_host, __remote_user, __remote_pwd = remoteDevice

        jumpCon = paramiko.SSHClient()
        jumpCon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        jumpCon.connect(__jump_host,username=__jump_user,password=__jump_pwd)

        jump_transport = jumpCon.get_transport()
        local_addr = (__jump_host, 22)
        dest_addr = (__remote_host, 22)
        jump_channel = jump_transport.open_channel("direct-tcpip",dest_addr,local_addr)

        # End device connection
        self.Ehost = paramiko.SSHClient()
        self.Ehost.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # end device connect
        self.Ehost.connect(__remote_host,username=__remote_user,password=__remote_pwd,sock=jump_channel)

        #


    def execute_cmd(self,cmd):
        stdin, stdout, stderr = self.Ehost.exec_command(cmd) #edited#
        pprint(stdout.read().decode('utf-8')) #edited#
