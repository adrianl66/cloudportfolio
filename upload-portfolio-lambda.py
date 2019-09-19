import boto3
from botocore.client import Config
import zipfile
import mimetypes
import io
import json

def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:ap-southeast-1:937336577693:deployPortfolioTopic')

    location = {
        "bucketName": 'a3isolutionsbuild',
        "objectKey": 'CodeBuild.zip'
    }

    try:
        job = event.get("CodePipeline.job")
        if job:
            for artifact in job["data"]["inputArtifacts"]:
                if artifact["name"] == "BuildArtifact":
                    location = artifact["location"]["s3Location"]

        print ('Building portfolio from ' + str(location))

        s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

        portfolio_bucket = s3.Bucket('www.a3isolutions.com')
        build_bucket = s3.Bucket(location["bucketName"])

        portfolio_zip = io.BytesIO()
        build_bucket.download_fileobj(location["objectKey"], portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm)
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

        print ('Completed copying files')
        topic.publish(Subject='Deploy Successful', Message='www.a3isolutions.com site deployed succesfully!')
        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job["id"])
    except:
        topic.publish(Subject='Deploy Failed', Message='www.a3isolutions.com site was NOT deployed succesfully')
        raise
