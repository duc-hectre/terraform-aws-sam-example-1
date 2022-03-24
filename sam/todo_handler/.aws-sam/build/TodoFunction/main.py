# import decimal
# import json

import os

import boto3
import simplejson as json

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

    sqs = boto3.client('sqs')

    dynamoDb = boto3.resource('dynamodb')

    table_name = os.environ["DYNAMO_TABLE_NAME"]
    # table = dynamoDb.Table("tf_sam_todo_table")
    table = dynamoDb.Table(table_name)
    print(table)

    if event["httpMethod"] == "POST":
        data = event["body"]
        print(data)

        if data:
            # queue_url = 'https://sqs.ap-southeast-1.amazonaws.com/983670951732/rf_sam_todo_queue'
            queue_url = os.environ["SQS_URL"]

            # Send message to SQS queue
            response = sqs.send_message(
                QueueUrl=queue_url,
                DelaySeconds=10,
                MessageBody=data
            )
            msgId = response['MessageId']
            if msgId:
                return {
                    "statusCode": 201,
                    "body": data,
                    # "body": msgId,
                }
            else:
                return {
                    "statusCode": 400,
                    "body": json.dumps({
                        "message": "cannot send message to queue",
                    }),
                }

        else:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "missing name arg",
                }),
            }
    else:
        response = table.scan()
        print(response)
        items = response['Items'] if response else {}
        return {
            "statusCode": 200,
            "body":  json.dumps(items) if items else "",
        }
