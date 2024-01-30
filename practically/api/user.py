from practically import Practically
from bs4 import BeautifulSoup

class User:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, 'html.parser')

    @property
    def email(self) -> str | None:
        html_input_elem = self.soup.find("input", {"id": "Email"})
        return html_input_elem['value'] if html_input_elem else None

    @property
    def first_name(self) -> str | None:
        html_input_elem = self.soup.find("input", {"id": "FirstName"})
        return html_input_elem['value'] if html_input_elem else None
        
    @property
    def last_name(self) -> str | None:
        html_input_elem = self.soup.find("input", {"id": "LastName"})
        return html_input_elem['value'] if html_input_elem else None

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
