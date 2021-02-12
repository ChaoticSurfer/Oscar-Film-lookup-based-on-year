# row-index-91 > div.col-sm-18.col-full-xs.countdown-item-content > div.row.countdown-item-title-bar > div.col-sm-20.col-full-xs


import requests
import bs4


def get_film_year(inp):
    url = "https://editorial.rottentomatoes.com/guide/oscars-best-and-worst-best-pictures/"

    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    l = soup.select(
        "div.col-sm-18.col-full-xs.countdown-item-content > div.row.countdown-item-title-bar > div.col-sm-20.col-full-xs")

    res = ""
    for i in l:
        if inp in i.text:
            name = i.select_one("a").text
            res += name
    return res
