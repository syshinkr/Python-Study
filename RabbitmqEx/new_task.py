# 두 번째 mq 예제 센더
import pika
import random

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

# durable 옵션으로 서버 실행이 중단되었다가 다시 실행될 때도 상태 유지시킴
channel.queue_declare(queue='task_queue', durable=True)

# 큐에 쌓아둘 메시지 리스트 만들기
# 총 100개의 메시지를 만들며 메시지는 1~10 사이 정수
msgs = [str(i) + ":" + str(random.randrange(1, 11)) for i in range(100)]


def send_msg(msg):
    channel.basic_public(exchange='', routing_key='task_queue', body=str(msg),
                         property=pika.BasicProperties(
                             # 메시지를 디스크에 저장해 사라지지 않게 함
                             # 즉, 서버가 다시 시작되어도 메시지는 살아남음
                             delivery_mode=2, )
                         )


for msg in msgs:
    send_msg(msg)
    print(" # 메시지를 보냈습니다: %r" %msg)


connection.close()
