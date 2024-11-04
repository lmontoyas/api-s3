import boto3

def lambda_handler(event, context):
    nombre_bucket = event["body"]["nombreBucket"]

    try:
        s3 = boto3.client("s3")
        s3.create_bucket(Bucket = nombre_bucket, ObjectOwnership = "BucketOwnerPreferred")
        s3.put_public_access_block(
            Bucket = nombre_bucket,
            PublicAccessBlockConfiguration = {
                'BlockPublicAcls': False,
                'IgnorePublicAcls': False,
                'BlockPublicPolicy': False,
                'RestrictPublicBuckets': False
            }
        )

        # Configura el ACL
        s3.put_bucket_acl(ACL='public-read-write', Bucket =nombre_bucket)

        return {
            'statusCode': 201,
            'body': nombre_bucket
        }
    
    except Exception as e:
        print(e)
        return {
            'statusCode': 400,
            'body': {'message': f'Error al crear el bucket: {str(e)}'}
        }