import pika

parameters = pika.URLParameters('amqp://scmdb:qFg9X9gBdDkLjYzC@10.100.7.1:5672')

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='test_routing_key', durable=True)

channel.basic_publish('',
                      'test_routing_key',
                      'message body value',
                      pika.BasicProperties(content_type='text/plain',
                                           delivery_mode=pika.DeliveryMode.Transient))

connection.close()