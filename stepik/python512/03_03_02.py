"""
[STEPIK]
Python: основы и применение https://stepik.org/512
03_03_02 Обзорно об интернете: http-запросы, html-страницы и requests
"""

"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, 
на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, 
которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, 
за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.

Пример HTML файла
<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:
mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
"""

import re
import requests

PATTERN = r'<a.*?href.*?=.*?[\"|\'](((.*?):\/\/)|(\.\.)|)(.*?)(\/|:|\"|\').*'

# DEBUG inputs https://pastebin.com/raw/2mie4QYa
domains = [split[4] for split in re.findall(PATTERN, requests.get(input()).text) if split]

for domain in sorted(set(domains)):
    print(domain)
