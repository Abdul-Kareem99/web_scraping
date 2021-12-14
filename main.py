import requests
import bs4

HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'ru,en;q=0.9',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Cookie': '_ym_d=1638028483; _ym_uid=16380284831002969016; _ga=GA1.2.1786197767.1638028484; hl=ru; fl=ru; __gads=ID=f2109a86373b47f5-2258ce6009cc00aa:T=1638028484:S=ALNI_MZDKpM6LxBVxdd9A9LHfnkn9ov6HQ; feature_streaming_comments=true; visited_articles=273089:250947:273115:74839; _gid=GA1.2.323979866.1639131132; _ym_isad=2; habr_web_home=ARTICLES_LIST_ALL',
           'Host': 'habr.com',
           'If-None-Match': 'W/"3b4e0-3d11MkVrV8wKQGJkLNaNzGDQwhY"',
           'Referer': 'https://gitpreview.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
           'sec-ch-ua': '"Chromium";v="94", "Yandex";v="21", ";Not A Brand";v="99"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Windows"',
           'Sec-Fetch-Dest': 'document',
           'Sec-Fetch-Mode': 'navigate',
           'Sec-Fetch-Site': 'same-origin',
           'Sec-Fetch-User': '?1',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.2.773 Yowser/2.5 Safari/537.36',
}


KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'финансы в it', 'физика', 'ltv'}
response = requests.get('https://habr.com/ru/all/', headers=HEADERS)
text = response.text
response.raise_for_status()

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    previews = article.find_all('div', class_="tm-article-snippet")
    content = []
    for text in previews:
        content.append(text.text)
    content = ' '.join(content).lower()
    for keyword in KEYWORDS:
        if keyword in content:
            span_title = article.find('a', class_='tm-article-snippet__title-link')
            title_name = span_title.find('span').text
            span_datetime = article.find('time')
            date = span_datetime['title']
            href = span_title['href']
            result = f'{date} - {title_name} - https://habr.com{href}'
            print(result)