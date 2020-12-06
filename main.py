import requests
import os
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        # """Метод загруджает файл file_path на яндекс диск"""
        # Тут ваша логика
        file_path = input('Введите имя файла для загрузки: ')
        resp = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                            params={'path': file_path, 'overwrite':'true'},
                            headers=self.token)
        answer = resp.json()
        pprint(answer)
        upload_link = answer['href']
        user_input = input('Введите имя файла, который вы хотите загрузить:\n')
        with open(user_input, 'rb') as f:
            resp1 = requests.put(upload_link, files={'file': f})
        resp1.raise_for_status()
        print('файл успешно загружен')

if __name__ == '__main__':
    uploader = YaUploader('<Your Yandex Disk token>')
    result = uploader.upload('c:\my_folder\file.txt')

print(os.getcwd())
