from bs4 import BeautifulSoup
from dataclasses import dataclass
import datetime
from .assignments import Assignments

@dataclass
class CalendarEntry:
    title: str
    start_time: datetime.date
    teacher_name: str

class Calendar:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, "html.parser")
        self.items = []

        element = self.soup.select("#container-wrapper > div.row")[0]
        for child in element.find_all("div", class_="card h-100"):
            title = child.find("div", class_="font-weight-bold text-uppercase mb-1 text-gray-800").text
            start_time, teacher_name = [x.text for x in child.find_all("div", class_="mb-0 text-gray-800")]
            self.items.append(CalendarEntry(title=title, start_time=Assignments.parse_date(start_time), teacher_name=teacher_name))

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)
