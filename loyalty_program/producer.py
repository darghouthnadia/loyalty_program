# skeleton file for the producer of loyalty program

import pika, json

params = pika.URLParameters('amqps://qwpgztzf:URdQupS0682gEE3gpSQaGOvJ5KAuiiNB@poodle.rmq2.cloudamqp.com/qwpgztzf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='brand', body=json.dumps(body), properties=properties)
