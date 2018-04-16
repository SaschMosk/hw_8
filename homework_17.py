import requests

APP_ID = 'b05c0f60c1e1453c915f723cff4614b3'
# AUTH_URL = 'https://oauth.yandex.ru/authorize'
# auth_data = {
#     'response_type': 'token',
#     'client_id': APP_ID
# }
# print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = 'AQAAAAANV0R4AATplT0QzwDz2kF7hBLfHgDz0e4'


class YaBase:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_counters(self):
        headers = self.get_headers()
        response = requests.get('https://api-metrika.yandex.ru/management/v1/counters', headers=headers)
        return [c['id'] for c in response.json()['counters']]


class Counter(YaBase):

    def __init__(self, counter_id, token):
        self.counter_id = counter_id
        super().__init__(token)

    def get_counter_stats(self):
        metrics = ['ym:s:visits', 'ym:pv:pageviews', 'ym:pv:users']
        headers = self.get_headers()
        responses = []
        for item in metrics:
            params = {
                'id': self.counter_id,
                'metrics': item
            }
            response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params,
                                    headers=headers)
            responses.append(response.json()['data'][0]['metrics'][0])
        output = dict()
        for m, r in zip(metrics, responses):
            output[m] = r
        return output


Base_1 = YaBase(TOKEN)

counter_1 = Base_1.get_counters()[0]
Counter_1 = Counter(counter_1, Base_1.token)

stats = Counter_1.get_counter_stats()
print(stats)
