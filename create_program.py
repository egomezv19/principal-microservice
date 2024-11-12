import boto3

def lambda_handler(event, context):
    # Obtener los datos del evento
    id_programa = event['body']['id_programa']
    pais_destino = event['body']['pais_destino']
    descripcion = event['body']['descripcion']
    fecha_inicio = event['body']['fecha_inicio']
    fecha_fin = event['body']['fecha_fin']
    
    # Inicializar el recurso de DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('programa')
    
    # Crear el ítem para DynamoDB
    programa = {
        'id_programa': id_programa,
        'pais_destino': pais_destino,
        'descripcion': descripcion,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin
    }
    # Insertar el ítem en DynamoDB
    response = table.put_item(Item=programa)
    
    # Retornar la respuesta
    return {
        'statusCode': 200,
        'body': response
    }
