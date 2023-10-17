import yaml
from utils import *

with open("config.yaml", "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

with open("auth.yaml", "r") as file:
    auth = yaml.load(file, Loader=yaml.FullLoader)

createCsv(name="data.csv")
for month in range(1, 13):
    n_days = getNumberOfDays(month)
    for day in range(1, n_days+1):
        current_day_data = []
        date, url = stringFormatDate(day, month, config["year"], config["website"])
        current_day_stories = parseMainArchivePage(url, use_proxy=True, proxy_details=auth)

        for current_day_story in current_day_stories:
            current_day_story_data = []

            vals = parseIndividualDayStory(current_day_story, use_proxy=True, proxy_details=auth)
            if vals is None: continue

            author_url, reading_time, title, subtitle, \
            claps, responses, story_url, story_paragraphs, \
            section_titles, number_sections, number_paragraphs, topics_names = vals

            current_day_story_data.append(date)
            current_day_story_data.append(title)
            current_day_story_data.append(subtitle)
            current_day_story_data.append(claps)
            current_day_story_data.append(responses)
            current_day_story_data.append(author_url)
            current_day_story_data.append(story_url)
            current_day_story_data.append(reading_time)
            current_day_story_data.append(number_sections)
            current_day_story_data.append(section_titles)
            current_day_story_data.append(number_paragraphs)
            current_day_story_data.append(story_paragraphs)
            current_day_story_data.append(topics_names)

            current_day_data.append(current_day_story_data)

        updateCsv(current_day_data, csv_file="data.csv")
        print(f'{len(current_day_stories)} stories scraped on {date}.')