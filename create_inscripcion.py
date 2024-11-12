import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Obtener los datos del evento
    id_estudiante = event['body']['id_estudiante']
    id_programa = event['body']['id_programa']
    estado_inscripcion = event['body'].get('estado_inscripcion', 'pendiente')
    
    # Generar la fecha de inscripción automáticamente
    fecha_inscripcion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Inicializar el recurso de DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('inscripciones')
    
    # Crear el ítem para DynamoDB
    inscripcion = {
        'id_estudiante': id_estudiante,
        'id_programa': id_programa,
        'fecha_inscripcion': fecha_inscripcion,
        'estado_inscripcion': estado_inscripcion
    }
    
    # Insertar el ítem en DynamoDB
    response = table.put_item(Item=inscripcion)
    
    # Retornar la respuesta
    return {
        'statusCode': 200,
        'body': 'Inscripción creada exitosamente'
    }
