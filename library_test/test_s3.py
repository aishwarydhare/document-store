from library import DocumentStore
from library.stores.s3 import S3Credentials

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

