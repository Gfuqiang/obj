from confluent_kafka import Consumer
import logging
logging.basicConfig(level=logging.DEBUG)

c = Consumer({
    'bootstrap.servers': '10.100.7.1:9092',
    'group.id': 'my_group1',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['zhiqian'])

while True:
    msg = c.poll(5)

    if msg is None:
        break
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()