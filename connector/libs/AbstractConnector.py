"""
    This is base connector to connect remote device
"""
from abc import ABC, abstractmethod


class BaseAgent(ABC):

    @abstractmethod
    def install_package(self):
        pass

    @abstractmethod
    def uninstall_package(self):
        pass