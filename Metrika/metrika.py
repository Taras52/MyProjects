import requests
from urllib.parse import urlencode
from pprint import pprint

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
    def __init__(self, token):
        self.token = token

    def get_counters(self):
        url = 'https://api-metrika.yandex.ru/management/v1/counters'
        headers = {
            'Authorization': 'OAuth {}'.format(self.token),
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers, params={'pretty': 1})
        return response.json()


taras52 = GetInfoFromMetrika(token_yam)
counters = taras52.get_counters()
pprint(counters)
