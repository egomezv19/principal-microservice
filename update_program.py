import boto3

def lambda_handler(event, context):
    # Obtener los datos del evento
    id_programa = event['body']['id_programa']
    fecha_inicio = event['body']['fecha_inicio']
    
    # Atributos a actualizar
    atributos = event['body']
    
    # Inicializar el recurso de DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('programa')
    
    # Construir la expresión de actualización
    update_expression = "SET " + ", ".join([f"{k} = :{k}" for k in atributos if k not in ['id_programa', 'fecha_inicio']])
    expression_values = {f":{k}": v for k, v in atributos.items() if k not in ['id_programa', 'fecha_inicio']}
    
    # Actualizar el ítem en DynamoDB
    response = table.update_item(
        Key={
            'id_programa': id_programa,
            'fecha_inicio': fecha_inicio
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_values
    )
    
    # Retornar la respuesta
    return {
        'statusCode': 200,
        'body': 'Programa actualizado exitosamente'
    }
