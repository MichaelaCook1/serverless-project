import logging
import requests
import azure.functions as func
from azure.cosmos import CosmosClient, PartitionKey, exceptions

endpoint = "https://mcook.documents.azure.com:443/"
key = "szscnN7yKEo6i67VVrUs88pkByKTV2Etiy9Q6QbGjRhHTQHPC9Pg3CQ39oAQyitxNwfcQAwv2QwcjcV59mcuaw=="
client = CosmosClient(endpoint, key)

database_name = "username"
database=client.create_database_if_not_exists(id=username)

container_name = "User"
container = database.create_container_if_not_exists(id=username, partition_key=PartitionKey(path="/username"), offer_throughput=400)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    letter= requests.get(https://serverlessproject-mcook.azurewebsites.net/api/LetterGen?code=yjdqO2mQsl8DMIbtLWNvXhtRF6UnVQYinYl1RuuX1rWa/PgCSzjDxQ==).text
    number= requests.get(https://serverlessproject-mcook.azurewebsites.net/api/NumberGen?code=eTIScavYqUaxlbkidXJFHvqo6lm2iqzteVgUQASTpJt9ujj/Aa0M6g==).text

    username = ""
    for i in range(5):
    username += letter[i]
    username += number[i]     

    username_to_add = {
        "id": username
    }
    container.create_item(body=username_to_add)

    return username  
