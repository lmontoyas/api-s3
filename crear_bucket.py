import boto3
import json

def lambda_handler(event, context):
    body = event.get('body', {})

    if isinstance(body, str):
        body = json.loads(body)

    nombre_bucket = body.get('nombre', '')

    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=nombre_bucket)
    return {
        'statusCode': 201,
        'message': f"{nombre_bucket} creado exitosamente"
    }
