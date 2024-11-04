import boto3

def lambda_handler(event, context):
    nombre_bucket = event['body']['nombreBucket']

    try:
        s3 = boto3.client("s3")
        s3.create_bucket(Bucket = nombre_bucket)
        
        return {
            'statusCode': 201,
            'message': f"{nombre_bucket} creado exitosamente"
        }
    
    except Exception as e:
        print(e)
        return {
            'statusCode': 400,
            'message': f"Error al crear el bucket: {str(e)}"
        }
