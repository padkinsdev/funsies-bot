import boto3

class AWSBucketManager:
  def __init__(self, bucket_name):
    self.client = boto3.client("s3")
    #self.bucket = boto3.Bucket(bucket_name)
  def get_as_file(self, fname):
    try:
      with open(fname, "wb") as item:
        self.client.download_fileobj(fname, item)
      return True
    except:
      return False
  def upload_file(self, fpath, fname):
    try:
      with open(fpath, "rb") as item:
        self.client.upload_fileobj(item, fname)
    except:
      return False
