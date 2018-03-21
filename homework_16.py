from urllib.parse import urlencode
import requests

#Получение токена
APP_ID = 6418314
AUTH_URL = 'https://oauth.vk.com/authorize'
auth_data = {
    'client_id': APP_ID,
    'display': 'mobile',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.73'
}
print('?'.join((AUTH_URL, urlencode(auth_data))))
TOKEN = '0412c0a564bf0df195826dd9c4f6a171008a46cff9cd9d8b73f8fc4ba529ca95ce39d23d06a507d84efca'

#Ввод списка id друзей общих, с которыми надо найти
friends = []
friend = input('Введите id друга для поиска обших. Если хотите завершить и найти общих для указанных введите stop:')


params = {
    'access_token': TOKEN,
    'v': '5.73',
    'target_uid': 156022171
}

response = requests.get('https://api.vk.com/method/friends.getMutual', params)
print(response.text)