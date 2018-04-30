import requests
import time
import json

TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'
version = 5.74


def get_user_id():
    user_input = input('Введите id или имя пользователя: ')
    if type(user_input) is int:
        user_id = user_input
        return user_id
    else:
        params = {
            'access_token': TOKEN,
            'v': version,
            'user_ids': user_input,
        }
        time.sleep(0.5)
        response = requests.get('https://api.vk.com/method/users.get', params, timeout=20)
        user_info = response.json()
        user_id = user_info['response'][0]['id']
        return user_id


def get_user_groups(user):

    params = {
        'access_token': TOKEN,
        'v': version,
        'user_id': user,
        'count': 1000
    }
    print('...')
    time.sleep(0.5)
    response = requests.get('https://api.vk.com/method/groups.get', params, timeout=20)
    groups_list = response.json()
    return groups_list['response']['items']


def get_user_fiends(user):

    params = {
        'access_token': TOKEN,
        'v': version,
        'user_id': user,
        'count': 1000
    }
    print('...')
    time.sleep(0.5)
    response = requests.get('https://api.vk.com/method/friends.get', params, timeout=20)
    friends_list = response.json()
    return friends_list['response']['items']


def match_group_members_with_friends(groups_list, friends_list):
    groups_without_users_friends = []
    for num, group_id in enumerate(groups_list):
        member_count = 0
        for i in range((len(friends_list)//200+1)):
            friends = ', '.join(str(fr) for fr in friends_list[(i*200):((i+1)*200)-1])
            params = {
                'access_token': TOKEN,
                'v': version,
                'group_id': group_id,
                'user_ids': friends
            }
            print('...')
            time.sleep(1.5)
            response = requests.get('https://api.vk.com/method/groups.isMember', params, timeout=30)
            membership = response.json()
            print(membership)
            try:
                for m in membership['response']:
                    if m['member'] == 1:
                        member_count += 1
            except:
                member_count += -1
            print(member_count)
        print("Обработано", num+1, "из", len(groups_list), 'групп')
        if member_count == 0:
            groups_without_users_friends.append(group_id)
        print(groups_without_users_friends)
    return groups_without_users_friends


def make_groups_list(groups):
    if groups != []:
        params = {
            'access_token': TOKEN,
            'v': version,
            'group_ids': ', '.join(str(gr) for gr in groups),
            'fields': ('name', 'id', 'members_count'),
        }
        print('...')
        time.sleep(0.5)
        response = requests.get('https://api.vk.com/method/groups.getById', params, timeout=20)
        groups_json = response.json()
        print(groups_json)
        groups_list = []
        for group in groups_json['response']:
            group_info = dict()
            group_info['name'] = group['name']
            group_info['gid'] = group['id']
            group_info['members_count'] = group['members_count']
            groups_list.append(group_info)
        with open('groups.json', 'w') as f:
            json.dump(groups_list, f,  skipkeys=True, ensure_ascii=False, indent=2)
        return groups_list
    else:
        print("Групп, в которых состоит только сам пользователь, нет.")


print(make_groups_list(match_group_members_with_friends(get_user_groups(get_user_id()),
                                                        get_user_fiends(get_user_id()))))
