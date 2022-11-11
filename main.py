#!/usr/bin/env python3
# coding: utf-8


import datetime
import random
import requests
import time
from bs4 import BeautifulSoup


CH_NUMBER = '*******'  # channel number
LINE_TOKEN = '*******************************************'  # LINE token
MESSAGE = 'ライブが開始されました'

def main():
    ch_url = 'https://live.line.me/channels/' + CH_NUMBER

    keyword = '"isBroadcastingNow":true'

    notify_url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + LINE_TOKEN}
    param = {'message': MESSAGE}

    while True:
        try:
            res = requests.get(ch_url)
            res.raise_for_status()  # エラーチェック
            soup = BeautifulSoup(res.content, "html.parser")
        except Exception as exc:
            print()
            print(exc)
            time.sleep(10)
            continue

        div = soup.find('div', id='data')

        if keyword in div['data-channel']:
            requests.post(notify_url, headers=headers, params=param)
            time.sleep(7200)

        # 待機
        sec = 180 + random.randint(-10, 10)
        time.sleep(sec)


if __name__ == "__main__":
    main()
