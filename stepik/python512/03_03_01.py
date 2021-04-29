"""
[STEPIK]
Python: основы и применение https://stepik.org/512
03_03_01 Обзорно об интернете: http-запросы, html-страницы и requests
"""

"""
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, 
возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход 
и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

Sample Input 1:
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 1:
Yes

Sample Input 2:
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample1.html

Sample Output 2:
No

Sample Input 3:
https://stepic.org/media/attachments/lesson/24472/sample1.html
https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 3:
Yes
"""

import re
import requests


def get_links_from_url(url: str) -> list:
    _links = list()
    res = requests.get(url)
    if res.status_code == 200 and res.text:
        _links = re.findall(r'<a.+href=\"(.+)\".*>', res.text)
    return _links


def is_related(a: str, b: str) -> bool:
    links = get_links_from_url(a)
    for link in links:
        if b in get_links_from_url(link):
            return True
    else:
        return False


print('Yes' if is_related(input(), input()) else 'No')
