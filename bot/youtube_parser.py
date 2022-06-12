import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import datetime
from lxml import html
import re
from utils import *
from constants import *


def channelid(ans):
    # to eliminate spaces between search queries with %20
    url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&q=' + ans + '&type=channel&key=' + apikey
    # Use yt API to give search results for username
    site1 = urlopen(url)
    # loads data to a json file format
    a1 = json.load(site1)
    # to get channelid and channelname using username
    ucid = str(a1.get("items")[0].get("id").get('channelId'))
    channelname = a1.get("items")[0].get("snippet").get('title')
    # returns channelid & channelname
    return (ucid, channelname)


def fetchsubs(url):
    site = urlopen(url)
    a = json.load(site)
    # returns subs count
    return (int(a.get("items")[0].get("statistics").get("subscriberCount")))


def fetch_number_of_youtube_subscribers(channel):
    channel_id, name = channelid(channel)
    url = u = 'https://www.googleapis.com/youtube/v3/channels?id=' + channel_id + '&key=' + apikey + '&part=statistics'
    subs = fetchsubs(url)

    data = {"youtube_channel": subs, "subscribers": name}
    headers = {"Content-Type": "application/json"}
    response = requests.post(restapi_url+'youtube', data=json.dumps(data), headers=headers)
    response.json()

    print('Youtube channel: ', subs, 'Has', str(name), 'Subscribers!!')