import boto3

sqs = boto3.client('sqs', region_name='eu-west-1')

def create_queue(queue_name):
    attributes = {
        'DelaySeconds': '0',                    
        'MessageRetentionPeriod': '86400',        
        'VisibilityTimeout': '30'                 
    }
    
    response = sqs.create_queue(
        QueueName=queue_name,
        Attributes=attributes
    )
    
    return response['QueueUrl']

def send_message(queue_url, message_body, message_attributes=None):
    kwargs = {
        'QueueUrl': queue_url,
        'MessageBody': message_body,
        'MessageAttributes': message_attributes or {}
    }
    
    response = sqs.send_message(**kwargs)
    return response['MessageId']

def delete_message(queue_url, receipt_handle):
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    print("Deleted")

def change_visibility_timeout(queue_url, receipt_handle, visibility_timeout):
    sqs.change_message_visibility(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle,
        VisibilityTimeout=visibility_timeout
    )
    print(f"Changed to {visibility_timeout} seconds")

def receive_message(queue_url):
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=['All'],
        MessageAttributeNames=['All'],
        MaxNumberOfMessages=1,
        VisibilityTimeout=60,  
        WaitTimeSeconds=20     
    )
    
    if 'Messages' in response:
        message = response['Messages'][0]
        message_body = message['Body']
        message_attributes = message.get('MessageAttributes', {})
        receipt_handle = message['ReceiptHandle']
        
        print(f"Received message: {message_body}")
        print(f"Message attributes: {message_attributes}")
       
        change_visibility_timeout(queue_url, receipt_handle, 60)
       
        delete_message(queue_url, receipt_handle)
    else:
        print("No messages in the queue")
