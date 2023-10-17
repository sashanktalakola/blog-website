import pandas as pd
import requests
from bs4 import BeautifulSoup

columns = ['date', 'title', 'subtitle', 'claps', 'responses', 'author_url', 'story_url',
               'reading_time (mins)', 'number_sections', 'section_titles', 'number_paragraphs', 'paragraphs']
def createCsv(name):
    df = pd.DataFrame(columns=columns)
    df.to_csv(name, index=False)

def updateCsv(new_data, csv_file):
    df = pd.read_csv(csv_file)
    new_df = pd.DataFrame(new_data, columns=columns)
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv(csv_file, index=False)


def getNumberOfDays(month):
    if month in [1, 3, 5, 7, 8, 10, 12]: n_days = 31
    elif month in [4, 6, 9, 11]: n_days = 30
    else: n_days = 28

    return n_days

def stringFormatDate(day, month, year, url):
    month, day = str(month), str(day)
    if len(month) == 1: month = f'0{month}'
    if len(day) == 1: day = f'0{day}'

    date = f'{month}/{day}/{year}'
    url = f'{url}/archive/{year}/{month}/{day}'

    return date, url

def proxyAuth(proxy_details):
    user_id = proxy_details["USER_ID"]
    password = proxy_details["PASSWORD"]
    proxy_url = proxy_details["PROXY_URL"]
    proxy_port = proxy_details["PROXY_PORT"]

    proxies = {
        "http": f"http://{user_id}:{password}@{proxy_url}:{proxy_port}/",
        "https": f"http://{user_id}:{password}@{proxy_url}:{proxy_port}/"
    }
    return proxies

def parseMainArchivePage(url, use_proxy=False, proxy_details=None):
    if use_proxy:
        proxies = proxyAuth(proxy_details)
        page = requests.get(url, proxies=proxies)
    else:
        page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    stories = soup.find_all('div', class_='streamItem streamItem--postPreview js-streamItem')
    return stories

def parseIndividualDayStory(story, use_proxy=False, proxy_details=None):
    author_box = story.find('div', class_='postMetaInline u-floatLeft u-sm-maxWidthFullWidth')
    author_url = author_box.find('a')['href']

    try: reading_time = author_box.find('span', class_='readingTime')['title']
    except: return None

    title = story.find('h3').text if story.find('h3') else '-'
    subtitle = story.find('h4').text if story.find('h4') else '-'

    claps_button = story.find('button', class_='button button--chromeless u-baseColor--buttonNormal js-multirecommendCountButton u-disablePointerEvents')
    if claps_button: claps = claps_button.text
    else: claps = 0

    responces_button = story.find('a', class_='button button--chromeless u-baseColor--buttonNormal')
    if responces_button: responses = responces_button.text
    else: responses = '0 responses'

    try: story_url = story.find('a', class_='button button--smaller button--chromeless u-baseColor--buttonNormal')['href']
    except: return None
    reading_time = reading_time.split()[0]
    responses = responses.split()[0]

    story_paragraphs, section_titles, number_sections, number_paragraphs = parseIndividualArticle(story_url, use_proxy, proxy_details)

    return author_url, reading_time, title, subtitle, claps, responses, story_url, story_paragraphs, section_titles, number_sections, number_paragraphs

def parseIndividualArticle(story_url, use_proxy=False, proxy_details=None):
    if use_proxy:
        proxies = proxyAuth(proxy_details)
        story_page = requests.get(story_url, proxies=proxies)
    else:
        story_page = requests.get(story_url)
    story_soup = BeautifulSoup(story_page.text, 'html.parser')

    sections = story_soup.find_all('section')
    story_paragraphs = []
    section_titles = []
    for section in sections:
        paragraphs = section.find_all('p')
        for paragraph in paragraphs:
            story_paragraphs.append(paragraph.text)

        subs = section.find_all('h1')
        for sub in subs:
            section_titles.append(sub.text)

    number_sections = len(section_titles)
    number_paragraphs = len(story_paragraphs)

    return story_paragraphs, section_titles, number_sections, number_paragraphs