from django import template
from bs4 import BeautifulSoup
import requests
register = template.Library()

url = 'https://sputnik.by/education/'
page = requests.get(url)

titles_list, dates_list, urls_list, image_list = [], [], [], []

soup = BeautifulSoup(page.text, 'lxml')

titles = soup.find_all('div', {'class': 'list__content'})
dates = soup.find_all('span', {'class': 'date'})
urls = soup.find_all('div', {'class': 'list__content'})
images = soup.find_all('div', {'class': 'list__image'})

for url in urls:
    href = url.find('a', {'class': 'list__title'}).get('href')
    result_url = ("https://sputnik.by" + href)
    urls_list.append(result_url)

for item in titles:
    result_title = item.text
    titles_list.append(result_title)

for datochka in dates:
    result_date = datochka.text
    dates_list.append(result_date)

for image in images:
    path = image.find('img', {'class': 'responsive_img m-list-img'}).get('src')
    image_list.append(path)

itog = []
for i in range(len(titles_list)):
    itog.append(f"{titles_list[i]} <br> <img src='{image_list[i]}' height='250'> <br> <br> <a class='btn btn-secondary' href='{urls_list[i]}'>Посмотреть статью</a> <br> ")


@register.simple_tag()
def news():
    return str(itog)

