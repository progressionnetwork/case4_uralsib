import json

import requests
import datetime
import vk # pip install py-vkontakte
from constants import *
import time


def get_vk_number_of_followers(account: str) -> str:
    response = requests.get('https://api.vk.com/method/groups.getMembers',
                            params={
                                'group_id': '35524999',
                                'access_token': vktoken,
                                'v': ver,
                                'domain': account,
                                'count': 10,
                            })
    res = response.json()
    #print(res)
    vk_subscribers = res['response']['count']
    data = {"vk_subscribers": vk_subscribers}
    headers = {"Content-Type": "application/json"}
    response = requests.post(restapi_url+'vk_subscribers', data=json.dumps(data), headers=headers)
    response.json()
    print ("Vk followers: ", vk_subscribers)


def get_vk_posts(account):
    offset = 0
    count = 25
    posts = []
    while offset < 100:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': vktoken,
                                    'v': ver,
                                    'domain': account,
                                    'count': count,
                                    'offset': offset
                                })
        data = response.json()['response']['items']
        offset += 100
        posts.extend(data)
        time.sleep(0.5)
    print(posts)
    total = len(posts)
    print('total posts', total)
    i = 1
    for post in posts:
        #try:
        print(i)
        print('id: ', post['id'])
        print('date: ', post['date'])
        print('likes: ', post['likes']['count'])
        print('comments: ', post['comments']['count'])
        print('views: ', post['views']['count'])
        print('reposts: ', post['reposts']['count'])
        print('text: ', post['text'])
        #except:
        #    pass

        data = {"vk_post_id": post['id'],
                "likes": post['likes']['count'],
                "comments": post['comments']['count'],
                "views": post['views']['count'],
                "reposts": post['reposts']['count'],
                "text": post['text']
                }
        headers = {"Content-Type": "application/json"}
        response = requests.post(restapi_url+'vk_posts', data=json.dumps(data), headers=headers)
        response.json()

        i += 1



    return total