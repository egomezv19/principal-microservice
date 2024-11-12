import boto3
import json

def lambda_handler(event, context):
    # Parseo del JSON de entrada
    body = json.loads(event['body'])
    
    # Conexión a DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_estudiantes')
    
    # Estructura del ítem a guardar, obteniendo todos los campos directamente del JSON de entrada
    estudiante = {
        'Universidad': body['Universidad'],
        'DNI': body['DNI'],
        'ID_Estudiante': body['ID_Estudiante'],
        'Nombre': body['Nombre'],
        'Email': body['Email'],
        'Fecha_Nacimiento': body['Fecha_Nacimiento'],
        'Carrera': body['Carrera'],
        'Telefono': body['Telefono']
    }
    
    # Guardar el ítem en DynamoDB
    response = table.put_item(Item=estudiante)
    
    # Respuesta
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Estudiante creado exitosamente',
            'response': response
        })
    }
