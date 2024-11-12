import boto3

def lambda_handler(event, context):
    # Obtener los datos del evento
    id_programa = event['body']['id_programa']
    fecha_inicio = event['body']['fecha_inicio']
    
    # Inicializar el recurso de DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('programa')
    
    # Eliminar el ítem de DynamoDB
    response = table.delete_item(
        Key={
            'id_programa': id_programa,
            'fecha_inicio': fecha_inicio
        }
    )
    
    # Retornar la respuesta
    return {
        'statusCode': 200,
        'body': 'Programa eliminado exitosamente'
    }
