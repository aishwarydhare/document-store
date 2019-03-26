from library import CredentialsBase
from library import DataStoreBase
from library.stores.s3 import S3DataStore, S3Credentials


class DocumentStore:
    def __init__(self, name: str, credentials: CredentialsBase):
        if name == 's3':
            if not isinstance(credentials, S3Credentials):
                raise TypeError('s3 data source for document store expects credentials of class S3Credentials')
            s3_credentials = S3Credentials(
                credentials.access_key,
                credentials.access_secret,
                credentials.region
            )
            self.store = S3DataStore(s3_credentials)
        elif name == 'mysql':
            # similar implementation for mysql
            pass
        elif name == 'local':
            # similar implementation for local disk
            pass
        else:
            raise BaseException('invalid data source provided')

    # for custom data store
    def create(self, data_store: DataStoreBase):
        self.store = data_store
        return self.store

    @property
    def store(self):
        return self._store

    @store.setter
    def store(self, value):
        self._store = value
