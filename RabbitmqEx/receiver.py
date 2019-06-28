import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')


# 큐에서 가져온 메시지를 처리할 콜백 함수를 만듦.
# 단순히 body를 가져와 출력
def callback(ch, method, properties, body):
    print(" # 메시지 받음: %r" % body)


# 메시지를 보낼 때 어떻게 할 것인지 설정
# 함수, 큐, 응답 여부(no_ack) 지정
channel.basic_consume(callback, queue='hello', no_ack=True)

print('# 메시지 대기 중. 종료하려면 CTRL + C 를 누르세요')

# 메시지 보내기 시작. 명시적으로 종료하기 전까지 계속 실행되면서
# 큐에 메시지가 들어올 때마다 callback이 메시지 처리
channel.start_consuming()

