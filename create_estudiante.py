import boto3

def lambda_handler(event, context):
    # Obtener los datos del evento
    universidad = event['body']['universidad']
    dni = event['body']['dni']
    id_estudiante = event['body']['id_estudiante']
    fecha_nacimiento = event['body']['fecha_nacimiento']
    carrera = event['body']['carrera']
    nombre = event['body']['nombre']
    email = event['body']['email']
    telefono = event['body']['telefono']
    
    # Inicializar el recurso de DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('estudiantes')
    
    # Crear el ítem para DynamoDB
    estudiante = {
        'universidad': universidad,
        'dni': dni,
        'id_estudiante': id_estudiante,
        'fecha_nacimiento': fecha_nacimiento,
        'carrera': carrera,
        'nombre': nombre,
        'email': email,
        'telefono': telefono
    }
    # Insertar el ítem en DynamoDB
    response = table.put_item(Item=estudiante)
    
    # Retornar la respuesta
    return {
        'statusCode': 200,
        'body': response
    }
