import boto3
import json
import os

def lambda_handler(event, context):
    print(event)

    print(event["Details"]["Parameters"]["Language"])

    language = event["Details"]["Parameters"]["Language"]

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DDB_TABLE_NAME'])


#    response = table.get_item(Key={'phoneNumber': phoneNumber})
#    print(response)
    return {
        'statusCode': 200,
#        'playrecordingDisclaimer': response["Item"]["playrecordingDisclaimer"],
#        'contactFlowARN': response["Item"]["contactFlowARN"],
#        'greetingMessage': response["Item"]["greetingMessage"],
#        'defaultQueueARN': response["Item"]["defaultQueueARN"]
    }
