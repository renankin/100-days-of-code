from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# print(soup.title.string)

response = requests.get(url="https://news.ycombinator.com/news")

website_content = response.text

soup = BeautifulSoup(website_content, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_links = []
article_texts = []
for article in articles:
    text = article.a.getText()
    link = article.a.get("href")
    article_texts.append(text)
    article_links.append(link)
article_scores = [
    int(score.getText().split()[0]) for score in
    soup.find_all(name="span", class_="score")
]

max_index = article_scores.index((max(article_scores)))
print(article_texts[max_index])

