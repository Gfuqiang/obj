import pika, time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method_frame, properties, body):
    print(f"ch: {ch}")
    print(f"method: {method_frame}")
    print(f"props: {properties}")
    print(f"body: {body}")
    print(" [x] Received %r" % (body,))
    time.sleep(15)
    time.sleep(str(body).count('.'))
    print(method_frame.delivery_tag)
    print(" [x] Done")

    # ch.basic_ack(delivery_tag=method.delivery_tag)
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)


# channel.basic_consume('hello', callback)
message = channel.basic_get('hello')
channel.basic_ack(delivery_tag=message[0].delivery_tag)
print(message[-1])

print(' [*] Waiting for messages. To exit press CTRL+C')
# channel.start_consuming()
connection.close()