# 두 번째 mq 예제 리시버
import pika
import time
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
    msg = str(body, "utf8").split(":")

    print(" # [%s] %s 메시지를 받았습니다 \n %r" % (datetime.datetime.now(), msg[0], body))

    # 받은 숫자대로 멈춤
    # 최대 1초 걸림
    time.sleep(int(str(msg[1]))/10)
    print(" # [%s] 완료했습니다 " % datetime.datetime.now())

    # 메시지 큐 서버에 완료했다는 응답을 보냄
    # 이 응답이 가야 새로운 큐가 새로운 메시지를 보내줌
    ch.basic_ack(delivery_tag = method.delivery_tag)

# 컨슈머는 메시지를 미리 가져오는데, 얼마나 가져오게 할지 결정
# 만약 이 설정이 없다면, 컨슈머가 큐에 메시지를 요청할 때 무제한으로 가져옴
# 또한 중간에 새로운 컨슈머를 실행하면 기존에 큐에 들어가 있던 메시지를 분배하지 않음
channel.basic_qos(prefetch_count=1)

# 이 클라이언트가 수립한 채널이 어떤 큐에서 어떤 함수로 메시지를 보낼지 결정
channel.basic_consume(callback, queue='task_queue')

# 메시지 처리 시작
channel.start_consuming()