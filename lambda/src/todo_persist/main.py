import json

import boto3

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    print(event)

    dynamoDb = boto3.resource('dynamodb')
    table = dynamoDb.Table("tf_sam_todo_table")

    body = event['Records'][0]['body']

    if body:
        data = json.loads(body)
        existItems = table.scan()
        print(type(existItems))
        count = len(existItems['Items']) + 1
        table.put_item(
            Item={'id': str(count), 'todo': data["todo"], 'status': "0"})
