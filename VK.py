import requests


def check_vk_response(response):
    json_response = response.json()
    if 'error' in json_response:
        error_code = json_response['error']['error_code']
        error_msg = json_response['error']['error_msg']
        raise requests.exceptions.HTTPError(f'VK API error {error_code}: {error_msg}')
    return json_response


def get_wall_upload_server(vk_group_id, vk_token):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {
        'group_id': vk_group_id,
        'access_token': vk_token,
        'v': 5.131
    }
    response = requests.get(url, params=params)
    json_response = check_vk_response(response)
    server_url = json_response['response']['upload_url']
    return server_url


def upload_image(server_url, filename):
    with open(('images/' + filename), 'rb') as file:
        files = {'photo': file}
        url = server_url
        response = requests.post(url, files=files)
    json_response = check_vk_response(response)
    return json_response


def save_wall_photo(vk_group_id, vk_token, photo_param, server_param, hash_param):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = {
        'group_id': vk_group_id,
        'access_token': vk_token,
        'photo': photo_param,
        'server': server_param,
        'hash': hash_param,
        'v': 5.131
    }
    response = requests.post(url, params=params)
    json_response = check_vk_response(response)
    return json_response


def publish_wall_post(vk_group_id, vk_token, owner_id, media_id, comic_comment):
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'owner_id': f'-{vk_group_id}',
        'access_token': vk_token,
        'from_group': 1,
        'attachments': f'photo{owner_id}_{media_id}',
        'message': comic_comment,
        'v': 5.131
    }
    response = requests.post(url, params=params)
    check_vk_response(response)
