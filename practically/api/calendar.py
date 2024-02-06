from bs4 import BeautifulSoup
from dataclasses import dataclass
import datetime

@dataclass
def CalendarEntry:
    title: str
    start_time: datetime.date
    teacher_name: str

class Calendar:
    def __init__():
        self.soup = BeautifulSoup(html, "html.parser")
        self.items = []
        self.populate()

    def populate(self):
        element = self.soup.select("#container-wrapper > div.row")[0]

        for child in element.find_all("div", class_="card h-100"):
            title = child.find("div", class_="font-weight-bold text-uppercase mb-1 text-gray-800")
            start_time, teacher_name = child.find_all("div", class_="mb-0 text-gray-800")


    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

