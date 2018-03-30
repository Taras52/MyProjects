import requests
from time import sleep
import os
import json


TOO_MANY_REQUESTS = 6
path_for_config = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
path_for_group = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'groups.json')


def do_request(url, parameters):
    base_params = {
        'v': VERSION,
        'access_token': TOKEN,
    }
    base_params.update(parameters)
    while True:
        response = requests.get(url, base_params)
        print('.', end='')
        data = response.json()
        if 'error' in data:
            if int(data['error']['error_code']) == TOO_MANY_REQUESTS:
                sleep(0.4)
                continue
            else:
                result = None
                break
        else:
            result = data['response']
            break
    print(' ')
    return result


def get_friends_list():
    params = {
        'user_id': VKID,
    }
    friends_ids = do_request('https://api.vk.com/method/friends.get', params)['items']
    return friends_ids


def get_group_by_friend_list(friend_list):
    group_idents = []
    for friend in friend_list:
        params = {
            'user_id': friend,
        }
        result = do_request('https://api.vk.com/method/groups.get', params)
        if result is None:
            continue
        else:
            group_idents.extend(result['items'])
    group_idents = set(group_idents)
    return group_idents


def unique_groups_detect(friends_groups):
    params = {
        'user_id': VKID,
    }
    users_groups = do_request('https://api.vk.com/method/groups.get', params)['items']
    users_groups = set(users_groups)
    unique_groups = users_groups - friends_groups
    unique_groups = list(unique_groups)
    return unique_groups


def get_unique_group_data(list_of_groups):
    result = ','.join([str(group) for group in list_of_groups])
    params = {
        'fields': 'members_count',
        'group_ids': result,
        'extended': 1
    }
    list_of_group = do_request('https://api.vk.com/method/groups.getById', params)
    list_of_group_final = []
    for group in list_of_group:
        dict_of_data = {'id': group['id'], 'name': group['name'], 'members_count': group['members_count']}
        list_of_group_final.append(dict_of_data)
    print('Количество уникальных групп пользователя {} - {}'.format(VKID, len(list_of_group_final)))
    return list_of_group_final


def write_result_to_json(group_list, file_path):
    with open(file_path, 'w') as resultfile:
        json.dump(group_list, resultfile, ensure_ascii=False)


with open(path_for_config, 'r') as f:
    config_data = json.loads(f.read())
    TOKEN = config_data['token']
    VKID = config_data['vkid']
    VERSION = config_data['version']

if __name__ == '__main__':
    friend_ids = get_friends_list()
    group_ids = get_group_by_friend_list(friend_ids)
    group_data = unique_groups_detect(group_ids)
    write_result_to_json(get_unique_group_data(group_data), path_for_group)
