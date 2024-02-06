from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Assignment:
    title: str
    pdf_url: str
    start_time: datetime
    end_time: datetime

class Assignments:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "html.parser")
        self.items = []

        for card in self.soup.select("div > div > div.card.h-100"):
            title_element = card.find("div", class_="font-weight-bold text-uppercase mb-1 text-gray-800")
            title = title_element.text.strip() if title_element else None

            pdf_url_element = card.select_one('a[href*="/v1/studentweb/readpdf/"]')
            pdf_url = self.get_pdf_url(pdf_url_element["href"]) if pdf_url_element else None

            start_time, end_time = [self.parse_date(date.text.strip()) for date in card.select("div.mb-0.text-gray-800")]

            assignment = Assignment(title=title, pdf_url=pdf_url, start_time=start_time, end_time=end_time)
            self.items.append(assignment)

    @staticmethod
    def get_pdf_url(url):
        parsed_url = urlparse(url)
        id = parsed_url.path.split("/").pop()
        return f"https://teach.practically.com/v1/files/shared/content/{id[:2]}/{id}/{id}.pdf"

    @staticmethod
    def parse_date(s: str):
        return datetime.strptime(
            re.sub(r"(\s+)|IST (\(.*\))", " ", s[s.find(":") + 1 :].strip()).strip(),
            "%d %b %Y %I:%M %p",
        )

    def __str__(self):
        return "\n".join([f"{item.title} starts at {item.start_time}" for item in self.items])

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)
