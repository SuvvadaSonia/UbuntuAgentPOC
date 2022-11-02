"""
    it is a connector and used to connect ubuntu machine

    # useful links  ---------------------
        https://parallel-ssh.readthedocs.io/en/latest/index.html
"""

# third party packages
from pssh.clients import ParallelSSHClient

# from pssh.utils import enable_debug_logger

if __name__ == "__main__":
    import sys
    sys.path.insert(0,'../')

# local packages
from connector.libs.AbstractConnector import BaseAgent
from connector.libs.ssh_utils import ProcessDataFactory


class UbuntuAgent(BaseAgent):

    def __init__(self, host: str, auth:tuple) -> None:
        super().__init__()
        __user, __pwd = auth
        self.device = {
            'hosts': [host,],
            'user': __user,
            'password': __pwd,
        }
        self.__connector = ParallelSSHClient(**self.device)
        # enable_debug_logger()

    def initial_packages_required(self):
        """
            It installs packages which required for Ubuntu remote Agent
        """
        try:
            output = self.__connector.run_command('apt-get install -y wget', sudo=True)

            return ProcessDataFactory('India@123').loop_output(output, sudo=True)

        except Exception as e:
            print(e)

    def install_package(self, url):
        """
            It downloads installer file using wget and installs the bash script
        """
        try:
            # installing initial packages required
            return self.initial_packages_required()

        except Exception as e:
            print(e)

    def uninstall_package(self):
        return super().uninstall_package()

    def getConfig(self):
        pass


if __name__ == "__main__":
    kwargs = {
        'host': 'god-virtualbox',
        'auth_username': 'god',
        'auth_password': 'India@123'
    }
    # Agent = UbuntuAgent(**kwargs)
    # output = Agent.install_package('wget')
    # print(output)
