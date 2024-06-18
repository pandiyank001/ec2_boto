from common import create_queue

queue_name = 'pandiyansqsdemo'
queue_url = create_queue(queue_name)
print(f"Queue URL: {queue_url}")
