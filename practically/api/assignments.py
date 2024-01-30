from bs4 import BeautifulSoup, Tag
from urllib.parse import urlparse, parse_qs
import re

from practically.utils import parse_str_as_datestring

pattern = re.compile(r"\s+")


def str_clean(input_str):
    return re.sub(pattern, " ", input_str)


class Assignment:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, "html.parser")

    @property
    def title(self):
        title_element = self.soup.find(
            "div", class_="font-weight-bold text-uppercase mb-1 text-gray-800"
        )
        return title_element.text.strip() if title_element else None

    @property
    def start_time(self):
        start_time_element = self.soup.select(
            "div.col-xl-3:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)"
        )
        return (
            parse_str_as_datestring(
                str_clean(start_time_element[0].text[11 + 1 :].strip())
            )
            if start_time_element
            else None
        )

    @property
    def end_time(self):
        end_time_element = self.soup.select(
            "div.col-xl-3:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)"
        )
        return (
            parse_str_as_datestring(
                str_clean(end_time_element[0].text[9 + 1 :].strip())
            )
            if end_time_element
            else None
        )

    def __str__(self):
        return f"{self.title} starts at {self.start_time}"

    @staticmethod
    def get_pdf_id_from_url(url):
        parsed_url = urlparse(url)
        id = parsed_url.path.split("/").pop()
        return id

    @property
    def attached_pdf_url(self):
        url = self.soup.select_one('a[href*="/v1/studentweb/readpdf/"]')
        if not url:
            return None
        id = Assignment.get_pdf_id_from_url(url["href"])
        return f"https://teach.practically.com/v1/files/shared/content/{id[:2]}/{id}/{id}.pdf"


class Assignments:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "html.parser")
        self.items = []
        self.__populate_with()

    def __populate_with(self):
        for child in self.soup.select("div > div > div.card.h-100 > div.card-body"):
            self.items.append(Assignment(str(child)))

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)
