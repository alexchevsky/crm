import json

def lambda_handler(event, context):
    # Event holds the details of the request
    payload = event["body"]  # this is the request payload
    headers = event["headers"]  # these are the request headers

    # Let's print these values to CloudWatch logs
    print("Payload:", json.dumps(payload))
    print("Headers:", json.dumps(headers))

    # TODO: Store these values to your desired storage (e.g. S3, RDS, DynamoDB)

    # The Lambda handler must return a response for the API Gateway
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully received the callback')
    }