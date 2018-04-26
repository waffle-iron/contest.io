from abc import ABCMeta, abstractmethod


class EndpointInterface(metaclass=ABCMeta):
    @property
    @abstractmethod
    def endpointURL(self):
        raise NotImplementedError

    @abstractmethod
    def get(self, tags=None):
        raise NotImplementedError
        
    @abstractmethod
    def insertToDatabase(self):
        raise NotImplementedError
