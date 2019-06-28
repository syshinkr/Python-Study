import requests

import datetime


def main():
    url = "https://hooks.slack.com/services/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https://hoo"

    text = "테스트 메시지, 시간 : " + str(datetime.datetime.now())

    payload = {
        "text": text
    }

    requests.post(url, json=payload)


if __name__ == "__main__":
    main()