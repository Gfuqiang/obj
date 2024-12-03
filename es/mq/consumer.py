import pika
credentials = pika.PlainCredentials('scmdb', 'qFg9X9gBdDkLjYzC')
# BlockingConnection:同步模式
connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.100.7.1', port=5672, virtual_host='/',credentials=credentials))
channel = connection.channel()
# 申明消息队列。当不确定⽣产者和消费者哪个先启动时，可以两边重复声明消息队列。
channel.queue_declare(queue='test_routing_key', durable=True)#,arguments={"x-queue-type": "stream"})
# 定义⼀个回调函数来处理消息队列中的消息，这⾥是打印出来
def callback(ch, method, properties, body):
    # ⼿动发送确认消息
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body.decode())
# 告诉⽣产者，消费者已收到消息
# 告诉rabbitmq，⽤callback来接收消息
# 默认情况下是要对消息进⾏确认的，以防⽌消息丢失。
# 此处将auto_ack明确指明为True，不对消息进⾏确认。

#channel.basicQos(10);
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='test_routing_key', on_message_callback=callback)
# auto_ack=True) # ⾃动发送确认消息
# 开始接收信息，并进⼊阻塞状态，队列⾥有信息才会调⽤callback进⾏处理
channel.start_consuming()