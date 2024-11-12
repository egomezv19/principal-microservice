import boto3
import json

def lambda_handler(event, context):
    # Obtener los datos del evento desde el cuerpo de la solicitud
    body = json.loads(event['body'])
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
    
    # Verificar si el ítem existe y devolverlo
    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item']),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Inscripción no encontrada'}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
