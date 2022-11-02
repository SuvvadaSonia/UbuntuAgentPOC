"""
    It connects to windows machine using WinRm
    and executes installer & uninstaller scripts

-----------------------
Author: Vinodh Adari - Software Engineer - vinodh.a@tessrac.com
CopyRights - Tessrac Innovations Pvt Ltd.

"""
import sys
from winrm import Session
# from winrm.exceptions import WinRMError
from typing import Dict
from requests.exceptions import ConnectionError
from urllib3.exceptions import MaxRetryError, NewConnectionError
if __name__ == "__main__":
    sys.path.insert(0,'../')

from connector.libs.AbstractConnector import BaseAgent

device_payload = Dict[
    str, Dict
]

class WinRmNtlmAgent(BaseAgent):

    def __init__(self, target:str, auth:tuple) -> None:
        super().__init__()
        try:
            _user, _pwd = auth

            self.__conn = Session(target, auth=(_user, _pwd))
        except (OSError, NewConnectionError, MaxRetryError, ConnectionError) as e:
            print(e)

    def getConfig(self):
        try:
            result = self.__conn.run_cmd('ipconfig')
            return result.std_out

        except (OSError, NewConnectionError, MaxRetryError, ConnectionError) as e:
            print(e)

    def install_package(self):
        return super().install_package()

    def uninstall_package(self):
        return super().uninstall_package()


if __name__ == "__main__":
    IP = '192.168.0.103'
    # IP = '169.254.57.232'
    HOSTNAME = 'vinod'
    PWD = 'Do0ordie17k*'
    # WinRmNtlmAgent(IP, HOSTNAME, PWD).getConfig()
    # p = Protocol(
    #     endpoint=f'http://{IP}:5985/wsman',
    #     transport='ntlm',
    #     username=HOSTNAME,
    #     password=PWD,
    #     server_cert_validation='ignore'
    #     )
    # shell_id = p.open_shell()s
    # command_id = p.run_command(shell_id, 'ipconfig', ['/all'])
    # std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
    # p.cleanup_command(shell_id, command_id)
    # p.close_shell(shell_id)

# """

    p = Session(IP, auth=(HOSTNAME, PWD))
    r = p.run_cmd('ipconfig', ['/all'])

    print(r.std_out)


# """
