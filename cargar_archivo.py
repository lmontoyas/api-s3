import boto3
import base64

def lambda_handler(event, context):
    # Obtener el nombre de bucket y directorio desde el path
    nombre_bucket = event["body"]['nombreBucket']
    nombre_directorio = event["body"]['nombreDirectorio']
    nombre_archivo = event["body"]['nombreArchivo']
    nombre_archivo_base64 = event["body"]['contenido']

    s3 = boto3.client('s3')

    # Decodificar el contenido en base64 a binario
    contenido = base64.b64decode(nombre_archivo_base64)

    # Subir el archivo a s3
    s3.put_object(
        Bucket = nombre_bucket, 
        Key = f"{nombre_directorio}/{nombre_archivo}",
        Body = contenido
        )
    
    return {
        'statusCode': 201,
        'body': 'Archivo cargado'
    }