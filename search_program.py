import boto3

def lambda_handler(event, context):
    # Obtener los datos del evento
    pais_destino = event['body']['pais_destino']
    fecha_inicio = event['body']['fecha_inicio']
    
    # Inicializar el recurso de DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('programa')
    
    # Obtener el ítem de DynamoDB
    response = table.get_item(
        Key={
            'pais_destino': pais_destino,
            'fecha_inicio': fecha_inicio
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
            'body': 'Programa no encontrado'
        }
