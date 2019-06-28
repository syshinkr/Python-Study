import pika

# 서버와 연결을 맺음
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# 연결 안에서 채널을 만듦
channel = connection.channel()

# 채널 안에서 큐 선언. (새 큐 만들기)
channel.queue_declare(queue='hello')

# 메시지를 보냄.
channel.basic_public(exchange='', routing_key='hello', body='Hello world!')
print("메시지를 보냈습니다.")

# 서버와의 연결을 끊음
connection.close()

