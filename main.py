import requests
def intel(hero_list):
    url = "https://akabab.github.io/superhero-api/api/"
    uri = "/all.json"
    hero_int = {}
    intelligence = 0
    resp = requests.get(url + uri).json()
    for i in resp:
        str(i)
        hero_int[i["name"]] = i["powerstats"]["intelligence"]
    for i in hero_list:
        if hero_int[i] > intelligence:
            intelligence = hero_int[i]
            res = i
    print(f"{res} самый умный герой, его интелект = {intelligence}")
intel(['Hulk', 'Captain America', 'Thanos'])

import requests


class Yandex:

    host = "https://cloud-api.yandex.net:443/"
    def __init__(self, token):
        self.token = token
    def get_headers(self):
        return {"Content-Type" : "application/json",
                "Authorization" : f"OAuth {self.token}"}
    def get_files_list(self):
        uri = "v1/disk/resources/files/"
        request_url = self.host + uri
        params = {"limit":2}
        res = requests.get(request_url, headers= self.get_headers(), params= params)
        print(res.json())
    def get_link_for_upload(self, path):
        uri = "v1/disk/resources/upload/"
        request_url = self.host + uri
        params = {"path": path, "overwrite": True}
        res = requests.get(request_url, headers= self.get_headers(), params= params)
        print(res.json())
        return res.json()['href']
    def upload_to_disk(self,lokal_path,):
        ya_path =  "/" + lokal_path.split("\\")[-1]
        Upload_url = self.get_link_for_upload(ya_path)
        res = requests.put(Upload_url, data= open(lokal_path, 'rb'), headers= self.get_headers())
        if res.status_code == 201:
            print("Загрузка прошла успешна")
        else:
            print("Загрузка не удалась")

if __name__ == "__main__":
    TOKEN = str(input("Введите токен >>> "))
    path_to_file = str(input("Для загрузки пожалуйста введите полный путь до файла >>> "))
    ya = Yandex(TOKEN)
    ya.upload_to_disk(f"{path_to_file}")