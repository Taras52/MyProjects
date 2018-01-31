from urllib.parse import urlencode
import requests
import time

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


def common_friends_in_list(list_of_friends, add_data):
    common_friends = []
    for f in list_of_friends:
        param = {
            'access_token': token,
            'target_uid': f,
        }
        match_friends = requests.get('https://api.vk.com/method/friends.getMutual', params=param)
        common_friends_json = match_friends.json()
        if 'error' in match_friends.json().keys():
            continue
        common_friends += common_friends_json['response']
    time.sleep(1)
    common_friends = list(set(common_friends))
    print(len(common_friends))
    uid_and_domain = []
    for f in add_data['response']:
        if f['uid'] in common_friends:
            uid_and_domain.append({f['uid']: 'https://vk.com/' + f['domain']})
    return uid_and_domain


token = '***'  # put your token instead
params = {
    'access_token': token,
    'fields': 'domain'
}
response = requests.get('https://api.vk.com/method/friends.get', params=params)
friends_list = response.json()
friends_ids = []
for friend in friends_list['response']:
    friends_ids.append(friend['uid'])
print(common_friends_in_list(friends_ids, friends_list))
