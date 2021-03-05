import json
import requests
import datetime
from bs4 import BeautifulSoup
import urllib.request as req
file = open('info.json', 'r') #jsonファイルの読み込み(json形式ではない)
info = json.load(file) #json形式で読み込み(json形式に直す)
info['CHANNEL_ACCES_TOKEN']
from linebot import LineBotApi #LineBot作成用
from linebot.models import TextSendMessage
CHANNEL_ACCES_TOKEN = info['CHANNEL_ACCES_TOKEN'] #トークンを変数で定義
line_bot_api = LineBotApi(CHANNEL_ACCES_TOKEN) #インスタンス化
def getTrain(URL):
    # 運行状況を取得する
    response = req.urlopen(URL)
    parse_html = BeautifulSoup(response, 'html.parser')
    ul_lists=parse_html.find_all(class_="unko_status")
    ul_list=[]
    for i in ul_lists:
        ul_list.append(i.text)
    print(ul_list[2])
    return ul_list[2][0:12]
def main():
    USER_ID = info['USER_ID'] #IDを変数に代入
    url = "https://trafficinfo.westjr.co.jp/sp/chugoku.html"
    trainTime = getTrain(URL)
    messages = TextSendMessage(text='【～山陰本線の運行状況～】\n\n' + trainTime + url)
    line_bot_api.push_message(USER_ID, messages=messages) #メッセージ送信

if __name__ == "__main__":
    main()