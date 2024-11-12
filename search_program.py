import boto3
import json

# Inicializar el cliente de DynamoDB
dynamodb = boto3.client('dynamodb')

def search_program(event, context):
    # Obtener el cuerpo de la solicitud
    body = json.loads(event.get("body", "{}"))
    
    # Buscar un programa en DynamoDB
    response = dynamodb.get_item(
        TableName="programa",
        Key={
            "pais_destino": {"S": body["pais_destino"]},
            "fecha_inicio": {"S": body["fecha_inicio"]}
        }
    )
    
    item = response.get("Item")
    if item:
        # Formatear el elemento encontrado en una respuesta JSON
        program_data = {k: list(v.values())[0] for k, v in item.items()}
        return {
            "statusCode": 200,
            "body": json.dumps({"programa": program_data}),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Programa no encontrado"}),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }
