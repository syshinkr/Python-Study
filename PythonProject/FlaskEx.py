import json
import sqlite3

from flask import Flask
from flask import request

app = Flask(__name__)

app.debug = True


@app.route("/")
# 모든 데이터를 내려받기 위한 hello() 함수 정의
def hello():
    # con이라는 변수를 생성해 데이터베이스를 연결합니다
    with get_db_con() as con:
        cur = con.cursor()

        # hanbit_books 데이터베이스의 모든 데이터 선택
        q = "select * from hanbit_books"
        result = cur.execute(q)

    # 결과를 JSON 문자열로 만들어줌
    result_json = jsonize(result)

    # 결과를 불러옴
    return result_json


# name 을 파라미터로 받기
@app.route("/hello/<name>")
def hello_to(name):
    return "Hello {}".format(name)


@app.route("/hello")
def hello_to_get_param():
    # /hello?name=miku 와 같은 형식의 요청을 받아
    # ?name=<이름>의 값이 오면, <이름>을 name 에 저장합니다
    name = request.args.get("name")
    return "Hello,{}".format(name)


def get_db_con() -> sqlite3.connect:
    return sqlite3.connect("db.sqlite")


@app.route("/books/by/author")
def get_books_by_author():
    name = request.args.get("name")

    # 데이터베이스 연결을 가져와서 작업
    # 작업이 끝나면 자동으로 with가 close 호출
    with get_db_con() as con:
        # 커서를 가져옴
        cur = con.cursor()

        # 쿼리 작성. hanbit_books 테이블에서
        # author 열이 name과 일치하는 걸 찾아옴
        q = "SELECT * FROM hanbit_books WHERE author LIKE :name ORDER BY title"
        param = {
            "name": "%" + name + "%"
        }

        result = cur.execute(q, param)

    # 결과를 JSON 문자열로 만들어줌
    result_json = jsonize(result)

    return result_json


@app.route("/books/by/month")
def get_books_by_month():
    month = request.args.get("month")

    # 숫자가 한 자리인 경우, 앞에 "0"을 붙여줌
    if int(month) < 10:
        month = "0" + month

    with get_db_con() as con:
        cur = con.cursor()

        # 쿼리 작성. hanbit_books 테이블에서 pub_date 열의
        # 월 부분이 month와 일치하는 걸 찾아옴
        q = "SELECT * FROM hanbit_books WHERE strftime('%m', pub_date) = :month ORDER BY pub_date DESC"
        param = {
            "month": month
        }

        result = cur.execute(q, param)

    result_json = jsonize(result)

    return result_json


def jsonize(result):
    result_json = json.dumps(list(result.fetchall()),
                             ensure_ascii=False).encode("utf-8")

    return result_json


if __name__ == "__main__":
    app.run()
