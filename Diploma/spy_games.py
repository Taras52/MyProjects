import requests
import time
import os
import json


def get_friends_list(vk_id, acc_token):
    params = {
        'access_token': acc_token,
        'user_id': vk_id,
        'v': '5.73'
    }
    response = requests.get('https://api.vk.com/method/friends.get', params=params)
    friends_list = response.json()
    friends_ids = friends_list['response']['items']
    return friends_ids


def get_groups_by_friend_list(friend_list, acc_token):
    group_ids = []
    for friend in [8822, 20338, 31769, 68120, 179265, 195320, 265528, 292699, 295473, 314089]:
        params = {
            'access_token': acc_token,
            'user_id': friend,
            'v': '5.73'
        }
        response = requests.get('https://api.vk.com/method/groups.get', params=params)
        print('.', end='')
        group_list = response.json()
        if 'error' in response.json().keys():
            continue
        group_ids.extend(group_list['response']['items'])
        time.sleep(0.4)
    print(' ')
    group_ids = set(group_ids)
    return group_ids


def output_unique_groups(vk_id, friends_groups, acc_token, filepath):
    params = {
        'access_token': acc_token,
        'user_id': vk_id,
        'v': '5.73',
    }
    response = requests.get('https://api.vk.com/method/groups.get', params=params)
    group_list = response.json()
    users_groups = group_list['response']['items']
    users_groups = set(users_groups)
    unique_groups = users_groups - friends_groups
    unique_groups = list(unique_groups)
    result = ','.join([str(group) for group in unique_groups])
    params = {
        'access_token': acc_token,
        'user_id': vk_id,
        'fields': 'id, name, members_count',
        'v': '5.73',
        'group_ids': result,
    }
    response = requests.get('https://api.vk.com/method/groups.getById', params=params)
    group_info = response.json()
    print(group_info)
    list_of_group = group_info['response']
    list_of_group_final = []
    for f in list_of_group:
        dict_of_data = {'id': f['id'], 'name': f['name']}
        list_of_group_final.append(dict_of_data)
    with open(filepath, 'w') as f:
        f.write(json.dumps(list_of_group_final, ensure_ascii=False))


vkid = 5030613  # user id at vk.com
token = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'
path_for_group = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'groups.json')
print(get_groups_by_friend_list(get_friends_list(vkid, token), token))
print(output_unique_groups(vkid, get_groups_by_friend_list(get_friends_list(vkid, token), token), token, path_for_group))
