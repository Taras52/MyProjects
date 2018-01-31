from urllib.parse import urlencode
import requests

app_id = 6353339
oauth_url = 'https://oauth.vk.com/authorize'
auth_data = {
    'client_id': app_id,
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.71',
}
# print('?'.join((oauth_url, urlencode(auth_data))))


def common_friends_in_list(list_of_friends):
    common_friends = []
    for friend in list_of_friends:
        param = {
            'access_token': token,
            'target_uid': friend,
        }
        match_friends = requests.get('https://api.vk.com/method/friends.getMutual', params=param)
        common_friends_json = match_friends.json()
        print(common_friends_json)
        common_friends += common_friends_json['response']
        print(common_friends)
    common_friends = list(set(common_friends))
    return common_friends


token = '******'  # put your token instead
params = {
    'access_token': token,
}
response = requests.get('https://api.vk.com/method/friends.get', params=params)
friends_list = response.json()
print(friends_list)
print(common_friends_in_list(friends_list['response']))
