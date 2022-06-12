import json
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import datetime
from lxml import html
import re
from utils import *
from constants import *


def fetch_number_of_subscribers(channel):
    page = requests.get('https://t.me/' + channel, timeout=8).text
    doc = html.fromstring(page)
    try:
        div = doc.xpath("//div[@class='tgme_page_extra']")[0]
    except IndexError:
        raise Exception('Not a group/channel')
    member_str = div.text_content()
    # members = group
    # subscribers = channel
    if 'members' not in member_str and 'subscribers' not in member_str:
        raise Exception('Not a group/channel')
    # Groups also give info about online members. Remove it: 30 members, 4 online -> 30 members
    nr = member_str.split(',')[0]
    # Clean spaces within the number: 1 084 members -> 1084 members
    return re.sub(r' (\d)', r'\1', nr)


def get_telegram_channel_subscribers(channel):
    nr = fetch_number_of_subscribers(channel)

    data = {"tg_subscribers": nr}
    headers = {"Content-Type": "application/json"}
    response = requests.post(restapi_url+'tg', data=json.dumps(data), headers=headers)
    response.json()

    print('Telegram channel: ', nr)
    return save_in_db(channel, nr)