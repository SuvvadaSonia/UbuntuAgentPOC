""" Ubuntu Agent POC 
Author by: Suvvada Sonia

"""

"""
    It connects to remote network device and runs installer scirpt and returns response to the ESE server-gateway
"""
# from connector import Connector
from connector.Connectors.JumpServerConnection import SSHAgent



if __name__ == "__main__":

    obj = SSHAgent(jumpDevice=('192.168.0.94','vinod','Do0ordie17k*'),remoteDevice=('god-VirtualBox','god','India@123'))
    obj.execute_cmd('ls -l')

    # print(arr[0,1]['user'], arr.size)
    # pass
    # connObj = Connector('windows','192.168.0.105',('vinod','Do0ordie17k*')).GetConnObj()
    # if connObj:
    #     connObj.getConfig()
    # print(getsizeof(device_payload), ' ', device_payload)
    # print(getsizeof(arr), ' ', arr)
