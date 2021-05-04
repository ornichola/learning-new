"""
[STEPIK]
Python: основы и применение https://stepik.org/512
03_05_02 API
"""
import os

"""
В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, 
выведите их имена в лексикографическом порядке.

Работа с API Artsy

Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, для получения 
доступа к API необходимо зарегистрироваться в проекте, создать свое приложение, и получить уникальный ключ (или токен), 
и в дальнейшем все запросы к API осуществляются при помощи этого ключа.

Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу 
документации к API https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться, 
создать приложение, и получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы.

После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, 
как можно выполнить запрос и как выглядит ответ сервера. Мы приведем пример запроса на Python.

import requests
import json

client_id = '...'
client_secret = '...'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
 
Теперь все готово для получения информации о художниках. На стартовой странице документации есть пример того, 
как осуществляется запрос и как выглядит ответ сервера. Пример запроса на Python.
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

# разбираем ответ сервера
j = json.loads(r.text)


Примечание:
В качестве имени художника используется параметр sortable_name в кодировке UTF-8.

Пример входных данных:
4d8b92b34eb68a1b2c0003f4
537def3c139b21353f0006a6
4e2ed576477cc70001006f99

Пример выходных данных:
Abbott Mary
Warhol Andy
Abbas Hamra

Примечание для пользователей Windows
При открытии файла для записи на Windows по умолчанию используется кодировка CP1251, в то время как для записи имен на сайте используется кодировка UTF-8, что может привести к ошибке при попытке записать в файл имя с необычными символами. Вы можете использовать print, или аргумент encoding функции open.

У вас есть неограниченное число попыток.
Время одной попытки: 5 mins
"""

import json
import os
import requests


def __get_token() -> str:
    res = requests.post(
        "https://api.artsy.net/api/tokens/xapp_token",
        data={
            "client_id": os.environ.get('ARTSY_CLIENT_ID'),
            "client_secret": os.environ.get('ARTSY_CLIENT_SECRET')
        }
    )
    return json.loads(res.text).get('token')


def _get_artist_data(artist_id: str) -> dict:
    res = requests.get(
        f'https://api.artsy.net/api/artists/{artist_id}', 
        headers={"X-Xapp-Token": __get_token()}
    )
    return json.loads(res.text)


def get_artist_birth_year(artist_data: dict):
    return {artist_data.get('sortable_name'): artist_data.get('birthday')}


artists_with_birth_years = dict()
with open('03_05_02_dataset.txt') as f:
    artists = f.read().splitlines()
    for artist_id in artists:
        artists_with_birth_years.update(get_artist_birth_year(_get_artist_data(artist_id)))

for artist in sorted(artists_with_birth_years.items(), key=lambda x: (x[1], x[0])):
    print(artist[0])
