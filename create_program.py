import boto3
import json

# Inicializar el cliente de DynamoDB
dynamodb = boto3.client('dynamodb')

def create_program(event, context):
    # Obtener el cuerpo de la solicitud
    body = json.loads(event.get("body", "{}"))
    
    # Crear un programa en DynamoDB
    response = dynamodb.put_item(
        TableName="programa",
        Item={
            "pais_destino": {"S": body["pais_destino"]},
            "descripcion": {"S": body["descripcion"]},
            "fecha_inicio": {"S": body["fecha_inicio"]},
            "fecha_fin": {"S": body["fecha_fin"]}
        }
    )
    
    return {
        "statusCode": 201,
        "body": json.dumps({"message": "Programa creado exitosamente"}),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    }
