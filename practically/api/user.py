from bs4 import BeautifulSoup


class User:
    def __init__(self, html: str):
        self.soup = BeautifulSoup(html, 'html.parser')

    def _find_input_value(self, input_id: str) -> str | None:
        html_input_elem = self.soup.find("input", {"id": input_id})
        return html_input_elem['value'] if html_input_elem else None

    @property
    def email(self) -> str | None:
        return self._find_input_value("Email")

    @property
    def first_name(self) -> str | None:
        return self._find_input_value("FirstName")

    @property
    def last_name(self) -> str | None:
        return self._find_input_value("LastName")

    @property
    def phone_number(self) -> str | None:
        html_input_elem = self.soup.find("input", {"id": "Mobile"})
        raw_phone_number = html_input_elem['value'] if html_input_elem else None

        html_select_elem = self.soup.find("select", {"id": "country_code"})
        raw_country_code = html_select_elem.find(
            "option", {"selected": True}).text.strip() if html_select_elem else None

        return f"{raw_country_code} {raw_phone_number}" if raw_country_code else raw_phone_number

    @property
    def display_name(self) -> str | None:
        return self._find_input_value("DisplayName")

    @property
    def login_id(self) -> str | None:
        return self._find_input_value("LoginID")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
