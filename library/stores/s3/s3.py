from library.CredentialsBase import CredentialsBase
from library.DataStoreBase import DataStoreBase


class S3Credentials(CredentialsBase):

    def __init__(self, access_key: str, access_secret: str, region: str):
        super().__init__()
        self.access_key = access_key
        self.access_secret = access_secret
        self.region = region


class S3DataStore(DataStoreBase):

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

    def __init__(self, c: S3Credentials):
        super().__init__()
        self.credentials = c
        self.name = 's3'
        # init boto connection using credentials

    def upload(self, doc):
        # body to doc object on s3
        pass

    def get(self):
        # body to fetch and return object from s3
        pass

    def fetch_meta(self):
        # body to fetch meta data of object from s3
        pass

    def delete(self):
        # body to delete object from s3
        pass

    def list(self):
        # body to list objects on s3 bucket
        pass
