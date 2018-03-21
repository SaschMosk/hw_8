# from urllib.parse import urlencode
import requests

APP_ID = 6418314
AUTH_URL = 'https://oauth.vk.com/authorize'
auth_data = {
    'client_id': APP_ID,
    'display': 'mobile',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.73'
}
# print('?'.join((AUTH_URL, urlencode(auth_data))))
TOKEN = '0412c0a564bf0df195826dd9c4f6a171008a46cff9cd9d8b73f8fc4ba529ca95ce39d23d06a507d84efca'


def friends_for_matching():
    friends = []
    while True:
        friend = input('Введите id друга для поиска обших. Если хотите завершить и найти общих для указанных введите '
                       'stop:')
        if friend != 'stop':
            friends.append(friend)
        if friend == 'stop':
            break
    return friends


def get_mutual_friends_id(friends):
    params = {
        'access_token': TOKEN,
        'v': '5.73',
        'target_uids': friends
    }
    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    id_list = response.json()
    return id_list


def get_mutual_friends_links(id_list):
    links = []
    for i in id_list['response'][0]['common_friends']:
        links.append('https://vk.com/id{}'.format(i))
        for ident, link in zip(id_list['response'][0]['common_friends'], links):
            print('{} {}'.format(ident, link))


get_mutual_friends_links(get_mutual_friends_id(friends_for_matching()))
