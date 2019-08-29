import boto3

class AWSBucketManager:
  def __init__(self, bucket_name):
    self.client = boto3.client("s3")
    self.s3 = boto3.resource("s3")
    self.bucket = self.s3.Bucket(bucket_name)
  def get_as_file(self, fname):
    try:
      self.bucket.download_file(fname, "/tmp/"+fname)
      return True, ""
    except Exception as err:
      return False, err
  def upload_file(self, fobj, fname):
    try:
      self.bucket.upload_file(fobj, fname)
      return True, ""
    except Exception as err:
      return False, err
