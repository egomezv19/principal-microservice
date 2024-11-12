import boto3

def lambda_handler(event, context):
    # Acceder a id_estudiante y id_programa directamente
    body = event['body']
    id_estudiante = body['id_estudiante']
    id_programa = body['id_programa']
    
    # Inicializar el recurso de DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('inscripciones')
    
    # Obtener el ítem de DynamoDB
    response = table.get_item(
        Key={
            'id_estudiante': id_estudiante,
            'id_programa': id_programa
        }
    )
    
    # Verificar si el ítem existe y devolver todos los atributos de la inscripción
    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': response['Item']  # Devuelve directamente el objeto para que Lambda lo convierta en JSON
        }
    else:
        return {
            'statusCode': 404,
            'body': {"message": "Inscripción no encontrada"}
        }
