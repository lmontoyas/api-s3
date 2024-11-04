import boto3

def lambda_handler(event, context):
    nombre_bucket = event["body"]["nombreBucket"]
    nombre_directorio = event["body"]["nombreDirectorio"]

    try:
        s3 = boto3.client('s3')
        # Crear directorio en s3
        s3.put_objest(
            Bucket = nombre_bucket,
            Key = f"{nombre_directorio}/"
            )
        
        return {
            'statusCode': 201,
            'body': 'Directorio creado exitosamente'
        }
    
    except Exception as e:
        print(e)
        return {
            'statusCode': 400,
            'body': 'Error al crear el directorio'
        }