import boto3

def lambda_handler(event, context):
    # Obtener los datos del evento
    id_estudiante = event['body']['id_estudiante']
    dni = event['body']['dni']
    
    # Inicializar el recurso de DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('estudiantes')
    
    # Obtener el ítem de DynamoDB
    response = table.get_item(
        Key={
            'id_estudiante': id_estudiante,
            'dni': dni
        }
    )
    
    # Verificar si el ítem existe y devolverlo
    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': response['Item']
        }
    else:
        return {
            'statusCode': 404,
            'body': 'Estudiante no encontrado'
        }
