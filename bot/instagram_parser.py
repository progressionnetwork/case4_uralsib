#import instaloader

def parse_data(s):

    data = {}

    s = s.split("-")[0]
    s = s.split(" ")

    # assigning the values
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]

    # returning the dictionary
    return data


def fetch_instagram_number_of_followers(account: str) -> str:

    #Get instance
    L = instaloader.Instaloader()

    # Login or load session
    L.login(USER, PASSWORD)  # (login)
    L.interactive_login(USER)  # (ask password on terminal)
    L.load_session_from_file(USER)  # (load session created w/
    #  `instaloader -l USERNAME`)

    # Obtain profile metadata
    profile = instaloader.Profile.from_username(L.context, PROFILE)

    # Print list of followees
    for followee in profile.get_followees():
        print(followee.username)

    # STATUS_PAGE_BASE = 'https://www.instagram.com/'+account+'/'
    # page = requests.get(STATUS_PAGE_BASE, timeout=8).text
    # s = BeautifulSoup(page, "html.parser")
    # print(s)
    # meta = s.find("meta", property="og:description")
    # print(meta)
    # if meta:
    #     rez = parse_data(meta.attrs['content'])
    # else:
    #     rez = 0
    # return
    # doc = html.fromstring(page)
    # print(doc)
    # try:
    #     followed_by = doc.xpath('//div[@class="profile-counter"][text()="Followed by"]/span/text()')[0]
    # except IndexError:
    #     raise Exception('Not an account')
    # return followed_by.strip() + ' followers'