from library import DocumentStore
from library import DataStoreBase, CredentialsBase


class MyDataStoreCredential(CredentialsBase):
    def __init__(self, uname: str, passw: str, host: str, container: str):
        super().__init__()
        self.username = uname
        self.password = passw
        self.host = host
        self.container = container


class MyDataStore(DataStoreBase):
    @property
    def credentials(self):
        return self._credentials

    @property
    def name(self):
        return self._name

    @credentials.setter
    def credentials(self, value):
        self._credentials = value

    @name.setter
    def name(self, value):
        self._name = value

    def __init__(self, c: MyDataStoreCredential, n: str):
        super().__init__()
        self.credentials = c
        self.name = n

    def upload(self, doc):
        # user defined body
        pass

    def get(self):
        # user defined body
        pass

    def fetch_meta(self):
        # user defined body
        pass

    def delete(self):
        # user defined body
        pass


if __name__ == '__main__':
    my_store_credential = MyDataStoreCredential(
        uname='root',
        passw='mpass123',
        host='localhost',
        container='my-container'
    )
    store = DocumentStore(data_store=MyDataStore(my_store_credential, 'my-custom-store')).store

    #
    # now store can be used as following
    #
    # store.upload(doc=m_file)
    # store.get()
    # store.fetch_meta()
    # store.delete()
    # store.list()
    pass
