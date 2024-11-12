import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Obtener los datos del evento
    id_estudiante = event['body']['id_estudiante']
    id_programa = event['body']['id_programa']
    nuevo_estado = event['body'].get('estado_inscripcion', 'pendiente')
    
    # Generar la fecha de modificación automática (opcional)
    fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Inicializar el recurso de DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('inscripciones')
    
    # Actualizar el ítem en DynamoDB
    response = table.update_item(
        Key={
            'id_estudiante': id_estudiante,
            'id_programa': id_programa
        },
        UpdateExpression="SET estado_inscripcion = :estado, fecha_inscripcion = :fecha",
        ExpressionAttributeValues={
            ':estado': nuevo_estado,
            ':fecha': fecha_actualizacion
        }
    )
    
    # Retornar la respuesta
    return {
        'statusCode': 200,
        'body': 'Inscripción actualizada exitosamente'
    }
