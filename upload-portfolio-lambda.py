import boto3
from botocore.client import Config
import zipfile
import mimetypes
from io import StringIO

s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

portfolio_bucket = s3.Bucket('www.a3isolutions.com')
build_bucket = s3.Bucket('a3isolutionsbuild')

portfolio_zip = StringIO()
build_bucket.download_fileobj('a3isolutionsBuild.zip', portfolio_zip)

with zipfile.Zipfile(portfolio.zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        portfolio_bucket.upload_fileobj(obj, nm,
            ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
        portfolio_bucket.Object(nm).Acl().pu(ACL='public-read')
