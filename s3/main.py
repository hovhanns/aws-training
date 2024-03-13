import boto3

# work with a profile
session = boto3.Session(profile_name='personal')
s3 = session.resource('s3')

# show all buckets
for bucket in s3.buckets.all():
    print(bucket.name)

    # show all files in a bucket
    bucket = s3.Bucket(bucket.name)
    for obj in bucket.objects.all():
        print(obj.key)
        # download a file
        s3.meta.client.download_file(bucket.name,obj.key, 'test1.jpeg')
        # upload a file
        s3.meta.client.upload_file('test1.jpeg', bucket.name, 'test.jpeg')
        break






