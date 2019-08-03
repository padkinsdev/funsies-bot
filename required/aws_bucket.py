import boto3

class AWSBucketManager:
  def __init__(self, bucket_name):
    self.client = boto3.client("s3")
    self.s3 = boto3.resource("s3")
    self.bucket = self.s3.Bucket(bucket_name)
  def get_as_file(self, fname):
    try:
      with open(fname, 'wb') as item:
        self.bucket.download_fileobj(fname, item)
        return True, item
    except Exception as err:
      return None, err
  def upload_file(self, fobj, fname):
    try:
      self.bucket.upload_fileobj(fobj, fname)
      return True, ""
    except Exception as err:
      return False, err
