import logging
from random import randomint
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    numbergen=randomint(10000,99999)
    number=str(numbergen)
    return number