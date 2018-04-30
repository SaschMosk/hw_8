# from urllib.parse import urlencode
import requests
import time

#получение токена
APP_ID = 6418314
AUTH_URL = 'https://oauth.vk.com/authorize'
auth_data = {
    'client_id': APP_ID,
    'display': 'mobile',
    'scope': ('friends', 'groups'),
    'response_type': 'token',
    'v': '5.73'
}
# print('?'.join((AUTH_URL, urlencode(auth_data))))
TOKEN = '139d819855a590fd4440b2971e81113f4a3aa579d268ed42f439cea44330d59b1593a41856a13c7ea3384'


def get_user_id():
    user_input = input('Введите id или имя пользователя: ')
    if type(user_input) is int:
        user_id = user_input
        return user_id
    else:
        params = {
            'access_token': TOKEN,
            'v': '5.73',
            'user_ids': user_input,
        }
        response = requests.get('https://api.vk.com/method/users.get', params)
        user_info = response.json()
        user_id = user_info['response'][0]['id']
        return user_id


def get_user_groups(user):

    params = {
        'access_token': TOKEN,
        'v': '5.73',
        'user_id': user,
        'extended': 0,
        'fields': ('name', 'id', 'members_count'),
        'count': 1000
    }
    print('...')
    response = requests.get('https://api.vk.com/method/groups.get', params)
    groups_list = response.json()
    return groups_list['response']['items']


def get_user_fiends(user):

    params = {
        'access_token': TOKEN,
        'v': '5.73',
        'user_id': user,
        'count': 1000
    }
    print('...')
    response = requests.get('https://api.vk.com/method/friends.get', params)
    friends_list = response.json()
    return friends_list['response']['items']


def match_group_members_with_friends(groups_list, friends_list):
    groups_without_users_friends = []
    for group_id in groups_list:
        member_count = 0
        for i in range((len(friends_list)//200+1)):
            friends = ', '.join(str(fr) for fr in friends_list[(i*200):((i+1)*200)-1])
            params = {
                'access_token': TOKEN,
                'v': '5.73',
                'group_id': group_id,
                'user_ids': friends
            }
            print('...')
            response = requests.get('https://api.vk.com/method/groups.isMember', params)
            time.sleep(0.5)
            membership = response.json()
            for m in membership['response']:
                if m['member'] == 1:
                    member_count += 1
        if member_count == 0:
            groups_without_users_friends.append(group_id)
    return groups_without_users_friends


def make_groups_list(groups):
    params = {
        'access_token': TOKEN,
        'v': '5.73',
        'group_ids': ', '.join(str(gr) for gr in groups),
        'fields': ('name', 'id', 'members_count'),
    }
    print('...')
    response = requests.get('https://api.vk.com/method/groups.getById', params)
    groups_json = response.json()
    groups_list = []
    for group in groups_json['response']:
        group_info = dict()
        group_info['name'] = group['name']
        group_info['gid'] = group['id']
        group_info['members_count'] = group['members_count']
        groups_list.append(group_info)
    return groups_list


print(make_groups_list(match_group_members_with_friends(get_user_groups(get_user_id()), get_user_fiends(get_user_id()))))