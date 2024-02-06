from bs4 import BeautifulSoup
from dataclasses import dataclass
from practically.exceptions import *


@dataclass
class Classroom:
    classroom_id: str
    classroom_name: str
    classroom_owner_name: str


class Classrooms:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "html.parser")
        self._items = []

        for elem in self.soup.find_all("div", class_="col-xl-3 col-md-6 mb-4"):
            try:
                name_elem = elem.find("div", class_="font-weight-bold").text.strip()
                owner_elem = elem.find("div", class_="mb-0").text.strip()
                id_elem = elem.find("a")["href"].split("/").pop()

                self._items.append(
                    Classroom(
                        classroom_id=id_elem,
                        classroom_name=name_elem,
                        classroom_owner_name=owner_elem,
                    )
                )
            except AttributeError:
                raise MalformedHTMLException(
                    "Something went wrong when parsing HTML in Classrooms"
                )

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)
