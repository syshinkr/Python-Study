# celery 태스크 퍼블리셔

# 앞서 만든 테스크 코드
import tasks

# 태스크로 지정한 함수를 바로 호출하지 않음
result = tasks.add.delay(2, 2)

print('Get result')

print(result.get())

