import boto3
import json

def lambda_handler(event, context):
    # Parseo del JSON de entrada
    body = json.loads(event['body'])
    
    # Conexión a DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_programas')
    
    # Estructura del ítem a guardar, obteniendo todos los campos directamente del JSON de entrada
    programa = {
        'ID_Programa': body['ID_Programa'],
        'Universidad': body['Universidad'],
        'Nombre': body['Nombre'],
        'Descripcion': body['Descripcion'],
        'Fecha_Inicio': body['Fecha_Inicio'],
        'Fecha_Fin': body['Fecha_Fin'],
        'Pais_Destino': body['Pais_Destino'],
        'Requisitos': body['Requisitos']
    }
    
    # Guardar el ítem en DynamoDB
    response = table.put_item(Item=programa)
    
    # Respuesta
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Programa creado exitosamente',
            'response': response
        })
    }
