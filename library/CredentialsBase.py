import abc


class CredentialsBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError('users must define __init__ to use this base class')

