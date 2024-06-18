from common import send_message

queue_url = 'https://sqs.eu-west-1.amazonaws.com/975049934351/pandiyansqsdemo'  

message_body = 'PANDIYAN SQS'
message_attributes = {
    'Author': {
        'DataType': 'String',
        'StringValue': 'Pandiyan'
    },
    'Priority': {
        'DataType': 'Number',
        'StringValue': '1'
    }
}

message_id = send_message(queue_url, message_body, message_attributes)
print(f"Message sent with ID: {message_id}")
