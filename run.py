""" 
Ubuntu Agent POC 

It connects to windows machine using WinRm
and executes installer & uninstaller scripts

-----------------------
Author: Suvvada Sonia - Jr. Software Engineer - sonia.s@tessrac.com
CopyRights - Tessrac Innovations Pvt Ltd.

"""

from winrm import Session  # WinRM allows you to perform various management tasks remotely.


class UbuntuAgent:
    
    def __init__(self, target:str, auth:tuple) -> None:
        try:
            _user, _pwd = auth

            self.__conn = Session(target, auth=(_user, _pwd))
        except (OSError, ConnectionError) as e:
            print(e)

    def getConfig(self):
        try:
            result = self.__conn.run_cmd('ipconfig', ['/all'])
            return result.std_out

        except (OSError, ConnectionError) as e:
            print(e)


if __name__ == "__main__":
    IP = '192.168.1.105'
    HOSTNAME = 'Administrator'
    PWD = 'India@123'
    r = UbuntuAgent(IP, (HOSTNAME, PWD)).getConfig()

    print(r)




# s = winrm.Session('192.168.1.105', auth=('Administrator', 'India@123'))
# ip_config = s.run_cmd('ipconfig', ['/all'])         # for ip configuration
# cpu_util = s.run_cmd('wmic cpu get loadpercentage')          # for cpu utilization
# disk_space = s.run_cmd('wmic diskdrive get size')             # for disk space
# ram = s.run_cmd('wmic computersystem get totalphysicalmemory')     # for RAM size


# print((ip_config.std_out).strip())
# print("#############################")
# print((cpu_util.std_out).strip())
# print("#############################")
# print((disk_space.std_out).strip())
# print("#############################")
# print((ram.std_out).strip())


