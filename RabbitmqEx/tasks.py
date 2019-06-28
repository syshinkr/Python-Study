# celery 워커 서버
from celery import Celery


app = Celery(
    # 현재 모듈의 이름
    # 이 파라미터를 전달하면, 현재 모듈을 단독으로 실행할 때도 문제없도록 함
    'tasks',

    # 메시지 브로커의 주소. 프로토콜과 접속 정보를 적음
    # 여기서는 rabbitMQ 이므로, AMQP 형식의 주소 사용함
    broker='pyamqp://guest@localhost///',

    # 결과를 저장할 backend 지정. 주로 DB 지정함
    backend='db+sqlite://db.sqlite'
)

# @app.task 디코레이터를 붙여 이 함수가 태스크라는 것을 표시
@app.task
def add(x, y):
    return x + y
