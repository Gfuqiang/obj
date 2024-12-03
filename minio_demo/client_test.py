from boto3.session import Session
from botocore import exceptions


class S3Client:

    def __init__(self):
        self.init_client()
        self.__bucket = 'scmdb-user-upload'

    def init_client(self):
        endpoint_url = 'http://s3.scmdb-inc.cn:19000'
        access_key_id = 'ncJN2vsdpKGS'
        access_secret_access_key = 'LSuob2YF64ftGAhxQKMV35wv1nqiEH8a'
        _session = Session(
            aws_access_key_id=access_key_id,
            aws_secret_access_key=access_secret_access_key,
        )
        self._resource = _session.resource('s3', endpoint_url=endpoint_url)

    def bucket_exists(self):
        try:
            self._resource.meta.client.head_bucket(Bucket=self.__bucket)
            return True
        except exceptions.ClientError as E:
            err_code = int(E.response['Error']['Code'])
            if err_code == 404:
                return False

    def print_all_bucket(self):
        for bucket in self._resource.buckets.all():
            print(bucket)


if __name__ == '__main__':
    s3 = S3Client()
    print(s3.print_all_bucket())