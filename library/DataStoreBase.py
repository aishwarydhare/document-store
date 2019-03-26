import abc


class DataStoreBase(metaclass=abc.ABCMeta):
    @property
    def credentials(self):
        raise NotImplementedError

    @property
    def name(self):
        raise NotImplementedError

    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError('users must define __init__ to use this base class')

    @abc.abstractmethod
    def upload(self, doc):
        raise NotImplementedError('must define upload method to use this base class')

    @abc.abstractmethod
    def get(self):
        raise NotImplementedError('must define get method to use this base class')

    @abc.abstractmethod
    def fetch_meta(self):
        raise NotImplementedError('must define fetch_meta method to use this base class')

    @abc.abstractmethod
    def delete(self):
        raise NotImplementedError('must define delete method to use this base class')



