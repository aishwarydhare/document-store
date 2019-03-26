from library import DocumentStore
from library.stores.s3 import S3DataStore, S3Credentials
from library import DataStoreBase, CredentialsBase

if __name__ == '__main__':
    store = DocumentStore('s3', S3Credentials(
        access_key="my_aws_access_key",
        access_secret="my_aws_access_secret",
        region="access_region"
    )).store
    #
    # now store can be used as following
    #
    # store.upload(doc=m_file)
    # store.get()
    # store.fetch_meta()
    # store.delete()
    # store.list()
    pass


#
# or a custom user defined store can be implemented
#

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
