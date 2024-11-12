import boto3

def lambda_handler(event, context):
    # Obtener los datos del evento
    universidad = event['body']['universidad']
    id_estudiante = event['body']['id_estudiante']
    
    # Inicializar el recurso de DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('estudiantes')
    
    # Eliminar el ítem de DynamoDB
    response = table.delete_item(
        Key={
            'universidad': universidad,
            'id_estudiante': id_estudiante
        }
    )
    
    # Retornar la respuesta
    return {
        'statusCode': 200,
        'body': 'Estudiante eliminado exitosamente'
    }
