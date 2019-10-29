import requests, bs4
from datetime import datetime as dt
import datetime

#creates a datetime object that be later compared to he article dates
date_today = datetime.date.today()

#empty lists that will have contents added during the following loops, will be looped through to create email content
titles_raw = []
dates_raw = []
links_raw = []

#funtion taking up to four links from The Guardian whose articles were published on the date of the code running.
def guardian_articles(link):
    request = requests.get(link)
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    results_link = soup.find_all("a", attrs={"class": "u-faux-block-link__overlay js-headline-text"})
    results_title = soup.find_all("span", attrs={"class": "js-headline-text"})
    results_date = soup.find_all("time", attrs={"class": "fc-item__timestamp"})
    for i in range(0,2):
        link = results_link[i].get("href")
        title = results_title[i].text
        date = results_date[i].get("datetime")
        date_sliced = date[:10]
        date_object = dt.strptime(date_sliced, "%Y-%m-%d").date()
        if date_today == date_object:
            titles.append(title)
            dates.append(date_object)
            links.append(link)

#funtion taking up to four links from the BBC whose articles were published on the date of the code running.
def bbc_articles(link):
    request = requests.get(link)
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    results_link = soup.find_all("a", attrs={"class": "qa-heading-link lx-stream-post__header-link"})
    results_title = soup.find_all("span", attrs={"class": "lx-stream-post__header-text"})
    results_date = soup.find_all("span", attrs={"class": "qa-meta-date gs-u-mr gs-u-display-inline-block"})
    for i in range(0,2):
        link_raw = results_link[i].get("href")
        link = "www.bbc.co.uk" + link_raw
        title = results_title[i].text
        date = results_date[i].text
        date_object = dt.strptime("2019 " + date, "%Y %d %b").date()
        if date_today == date_object:
            titles.append(title)
            dates.append(date_object)
            links.append(link)
           
def telegraph_articles(link):
    request = requests.get(link)
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    results_link = soup.find_all("a", attrs={"class": "list-headline__link u-clickable-area__link"})
    results_title = soup.find_all("span", attrs={"class": "list-headline__text"})
    results_date = soup.find_all("time", attrs={"class": "card__date"})
    for i in range(0,2):
        raw_link = results_link[i].get("href")
        link = "www.telegraph.co.uk" + raw_link
        title = results_title[i].text
        date = results_date[i].text
        date_sliced = date[:11]
        date_object = dt.strptime(date_sliced, "%d %b %Y").date()
        if date_today == date_object:
            titles_raw.append(title)
            dates_raw.append(date_object)
            links_raw.append(link)

#calls the functions with different links to various topics
guardian_articles("https://www.theguardian.com/society/prisons-and-probation")
guardian_articles("https://www.theguardian.com/law/criminal-justice")
bbc_articles("https://www.bbc.co.uk/news/topics/cnx753jenwzt/prisons")
bbc_articles("https://www.bbc.co.uk/news/topics/cldy2dmy748t/crime")
telegraph_articles("https://www.telegraph.co.uk/prisons/")
telegraph_articles("https://www.telegraph.co.uk/crime/")

titles = list(dict.fromkeys(titles_raw))
dates = dates_raw
links = list(dict.fromkeys(links_raw))

print(titles)
print(dates)
print(links)








