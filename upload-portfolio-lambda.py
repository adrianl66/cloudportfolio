import boto3
from botocore.client import Config
import zipfile
import mimetypes
import io
import json

def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:ap-southeast-1:937336577693:deployPortfolioTopic')

    try:
        s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
        portfolio_bucket = s3.Bucket('www.a3isolutions.com')
        build_bucket = s3.Bucket('a3isolutionsbuild')

        portfolio_zip = io.BytesIO()
        build_bucket.download_fileobj('a3isolutionsBuild.zip', portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm)
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

        print ('Completed copying files')
        topic.publish(Subject='Deploy Successful', Message='www.a3isolutions.com site deployed succesfully!')

    except:
        topic.publish(Subject='Deploy Failed', Message='www.a3isolutions.com site was NOT deployed succesfully')
        raise
