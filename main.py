# import requests
# from bs4 import BeautifulSoup
#
# # Актуальные заголовки для HTTP-запроса
# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
# }
#
# try:
#     url = "https://itproger.com/"
#     session = requests.Session()
#     response = session.get(url, headers=headers)
#
#     # Проверяем статус ответа
#     if response.status_code == 200:
#         # Используем BeautifulSoup правильно
#         soup = BeautifulSoup(response.content, 'html.parser')
#         print(soup.prettify())  # Выводим красиво отформатированный HTML
#     else:
#         print(f"Error: Status code {response.status_code}")
# except requests.exceptions.RequestException as e:
#     print(f"Request error: {e}")
# except Exception as e:
#     print(f"Unexpected error: {e}")


import requests
from bs4 import BeautifulSoup as bs4

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

try:
    url = "https://itproger.com/"
    session = requests.Session()
    req = session.get(url, headers=headers)
    if req.status_code == 200:
        soup = bs4(req.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'article'})
        for div in divs:
            title = div.find('a').text
            href = div.find('a')['href']
            print("{} - https://itproger.com/{}".format(title, href))
    else:
        print("Error")
except Exception:
    print("Error URL")
