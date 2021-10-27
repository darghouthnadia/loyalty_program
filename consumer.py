# skeleton file for the consumer of loyalty program

import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from .loyalty_program.models import Brand

params = pika.URLParameters('amqps://qwpgztzf:URdQupS0682gEE3gpSQaGOvJ5KAuiiNB@poodle.rmq2.cloudamqp.com/qwpgztzf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='discountcode')


def callback(ch, method, properties, body):
    id = json.loads(body)
    brand = Brand.objects.get(id=id)
    brand.save()


channel.basic_consume(queue='discountcode', on_message_callback=callback, auto_ack=True)

channel.start_consuming()

channel.close()