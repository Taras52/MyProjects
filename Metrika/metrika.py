import requests
from urllib.parse import urlencode

counter_id = 47590042
app_id = 'a9f4c0ebce3f4f1eabb84eec093cb635'
callback_url = 'https://oauth.yandex.ru/verification_code'
auth_url = 'https://oauth.yandex.ru/authorize'
token_yam = 'AQAAAAAAIyzzAATMNevHnq0CEkMbjPcdR0n32ac'

auth_data = {
    'response_type': 'token',
    'client_id': app_id
}
# print('?'.join((auth_url, urlencode(auth_data))))


class GetInfoFromMetrika:
    def __init__(self, token, counter):
        self.token = token
        self.counter = counter

    def get_visits(self):
        url = 'https://api-metrika.yandex.ru/stat/v1/data'
        headers = {
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/json'
        }
        params = {
            'id': self.counter,
            'metrics': 'ym:s:visits, ym:s:pageviews, ym:s:users'
        }
        response = requests.get(url, params=params, headers=headers).json()
        return response.json()


taras52 = GetInfoFromMetrika(token_yam, '47590042')
visits = taras52.get_visits()
print('https://taras52.github.io:')
print('Визитов {} Просмотров {} Посетителей {}'.format(visits['totals'][0], visits['totals'][1], visits['totals'][2]))
