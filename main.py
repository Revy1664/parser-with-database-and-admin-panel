import json
import lxml
import requests
from time import sleep
from bs4 import BeautifulSoup as BS


def get_html(url: str):
    """
        Get html-code of page
    """

    try:
        session = requests.Session()
        resp = session.get(url)
    except Exception:
        sleep(5)
        resp = session.get(url)

    return resp.text


def get_soup(html: str):
    """
        Get need data from html-code
    """

    soup = BS(html, "lxml")
    blogs = soup.find("div", class_="list-view").find("div", class_="_default-grid_1uulc_206").find_all("article", class_="_card_8sstg_1 _card--autoheight-mobile_8sstg_388")

    data = []

    for blog in blogs:
        name = blog.find("a", class_="_card__title_8sstg_1").text
        url = blog.find("a", class_="_card__title_8sstg_1")["href"]

        data.append(
            {
                f"{name}": "https://stopgame.ru" + url
            }
        )

    return data


def main():
    url = "https://stopgame.ru/blogs/all"
    html = get_html(url)
    blogs = get_soup(html)

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(blogs, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
