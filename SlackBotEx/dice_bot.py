# bot이 반응할 수 있게 하는 디코레이터 함수들을 불러옴
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.dispatcher import Message

import random

# 무엇에 반응할지 잡아줄 수 있는 re(정규 표현식) 패키지를 불러옴
import re


# listen_to : 채널에서 오가는 모든 대화에 반응
# 데코레이터 함수의 첫 번째 파라미터는 정규 표현식, 두 번째 파라미터는 플래그
@listen_to("Hello", re.IGNORECASE)

# 첫 번째 파라미터는 디스패처의 메시지 클래스
# 반응해야 할 채널에 메시지를 보내는 함수 등이 존재
# 여기 없는 두 번째 이후의 파라미터는 앞 정규 표현식에 그룹이 있으면 매칭된 문자열이 들어감
# 개수 상한 없음. 그룹 숫자에 따라 파라미터를 더 늘리면 됨
def hello(msg: Message):
    # send 는 채널에 그냥 말함
    msg.send("World!!")


# respone_to 는 @을 이용해서 봇을 언급하여 멘션했을 경우에만 반응함.
# 나머지는 listen_to의 역할과 같음
@respond_to("hi", re.IGNORECASE)
def hi(msg: Message):
    # reply 는 해당 반응을 일으킨 사람에게 말함
    # listen_to 든 respond_to 든 말을 건 사람에게 대답함
    msg.reply("Thank you inmaj!!")


# roll 던지는횟수d숫자면체 형식
@listen_to("roll (\d*)d(\d+)", re.IGNORECASE)

# 메시지, 주사위를 던지는 횟수, 주사위 면체를 지정하는 파라미터 넣기
def roll(msg: Message, number_of_die: str, side_of_die: str):
    # 에러 처리는 한다면 여기에서 함
    if number_of_die <= 0:
        return "some error message"
    if side_of_die <= 1:
        return "some error message"

    # random.randrange(1, int(side_of_die), 1) : 주사위 한 개 굴리기
    # 1부터 side_of_die 사이의 정수를 하나 고름
    # range(int(number_of_die))는 number_of_die 까지만큼 for 문 실행
    roll_result = [random.randrange(1, int(side_of_die), 1)
                   for i in range(int(number_of_die))]

    roll_sum = sum(roll_result)

    msg.send(str(roll_result))
    msg.send(str(roll_sum))
