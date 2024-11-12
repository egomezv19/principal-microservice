import boto3

def lambda_handler(event, context):
    # Obtener los datos del evento
    universidad = event['body']['universidad']
    id_estudiante = event['body']['id_estudiante']
    
    # Atributos a actualizar
    atributos = event['body']
    
    # Inicializar el recurso de DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('estudiantes')
    
    # Construir la expresión de actualización
    update_expression = "SET " + ", ".join([f"{k} = :{k}" for k in atributos if k not in ['universidad', 'id_estudiante']])
    expression_values = {f":{k}": v for k, v in atributos.items() if k not in ['universidad', 'id_estudiante']}
    
    # Actualizar el ítem en DynamoDB
    response = table.update_item(
        Key={
            'universidad': universidad,
            'id_estudiante': id_estudiante
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_values
    )
    
    # Retornar la respuesta
    return {
        'statusCode': 200,
        'body': 'Estudiante actualizado exitosamente'
    }
