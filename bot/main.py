#!/usr/bin/env python3

import json
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import datetime
import os
import sys
import re
from lxml import html
from vk_parser import *
from telegram_parser import *
from youtube_parser import *
from instagram_parser import *
from utils import *
from constants import *
from pydblite import Base

if __name__ == '__main__':
    get_telegram_channel_subscribers(channel)
    fetch_number_of_youtube_subscribers(youtube)
    get_vk_number_of_followers(vk)
    get_vk_posts(vk)
    fetch_instagram_number_of_followers(inst)
