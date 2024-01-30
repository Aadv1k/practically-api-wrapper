from bs4 import BeautifulSoup


class Classroom:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "html.parser")

    @property
    def name(self):
        return self.soup.find("div", class_="font-weight-bold").text.strip() or None

    @property
    def owner(self):
        return self.soup.find("div", class_="mb-0").text.strip() or None

    @property
    def id(self):
        return self.soup.find("a")["href"].split("/").pop() or None


class Classrooms:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, "html.parser")
        self.items = []
        self.__populate_with()

    def __populate_with(self):
        for elem in self.soup.find_all("div", class_="col-xl-3 col-md-6 mb-4"):
            self.items.append(Classroom(str(elem)))

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)
