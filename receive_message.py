from common import receive_message
import time

queue_url = 'https://sqs.eu-west-1.amazonaws.com/975049934351/pandiyansqsdemo' 
receive_message(queue_url)
time.sleep(1)
