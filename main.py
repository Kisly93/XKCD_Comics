import os
import shutil
from pathlib import Path
from VK import get_wall_upload_server, upload_image, save_wall_photo, publish_wall_post
from dotenv import load_dotenv
from download_comics import save_img, download_random_comic, get_file_name


def main():
    Path('images').mkdir(parents=True, exist_ok=True)
    load_dotenv()
    vk_group_id = os.environ['VK_GROUP_ID']
    vk_token = os.environ['VK_TOKEN']
    try:
        json_comic = download_random_comic()
        img_url = json_comic['img']
        comic_comment = json_comic['alt']
        filename = get_file_name(img_url)
        save_img(img_url, filename)
        server_url = get_wall_upload_server(vk_group_id, vk_token)
        upload_image(server_url, filename)
        loaded_image_data = upload_image(server_url, filename)
        photo_param = loaded_image_data['photo']
        server_param = loaded_image_data['server']
        hash_param = loaded_image_data['hash']
        saved_photo_options = save_wall_photo(vk_group_id, vk_token, photo_param, server_param, hash_param)
        owner_id = saved_photo_options['response'][0]['owner_id']
        media_id = saved_photo_options['response'][0]['id']
        publish_wall_post(vk_group_id, vk_token, owner_id, media_id, comic_comment)


    finally:
        shutil.rmtree('images')


if __name__ == '__main__':
    main()
