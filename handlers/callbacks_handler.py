import json
import boto3
import time
import base64
from urllib.parse import parse_qs
from datetime import datetime

# Create an S3 client
s3 = boto3.client('s3')


def lambda_handler(event, context):
    # Event holds the details of the request

    # Get the current time as a datetime object
    now = datetime.now()
    # Format the datetime object as an ISO-formatted string
    iso_time = now.isoformat()

    # Define your bucket name and key
    bucket_name = 'crm-callbacks'  # replace with your bucket name
    key = f'cloudpayments-pay-{iso_time}.json'

    decoded_body = base64.b64decode(event['body']).decode()
    payload = {k: v[0] for k, v in parse_qs(decoded_body).items()}

    # Convert the payload and timestamp to a JSON-formatted string
    data = json.dumps({
        'timestamp': iso_time,
        'payload': payload,
    })

    # Store the data in S3
    s3.put_object(Body=data, Bucket=bucket_name, Key=key)

    return {
        'code': 0,
    }
