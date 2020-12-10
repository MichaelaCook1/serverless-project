import logging
import random
import string
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    lettergen=string.ascii_lowercase
    letter=''.join(random.choice(lettergen) for i in range(5))
    return letter
