import requests
import os
from .utils import str_to_md5
from .api.user import User
import pickle

class Practically:
    def __init__(self, base_url="https://teach.practically.com", session_file="session.pickle"):
        self.base_url = base_url
        self.session_id = None
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0"
        self.session_file = session_file

    def __dump_session(self):
        with open(self.session_file, "wb") as f:
            pickle.dump({
                "session_id": self.session_id
            }, f)

    def __load_session(self):
        try:
            with open(self.session_file, "rb") as f:
                data = pickle.load(f)
                session_id = data.get("session_id")

                if not session_id:
                    raise Exception

                return session_id
        except:
            return None

    def is_session_expired_or_invalid(self):
        try:
            res = requests.get(f"{self.base_url}/v1/studentweb/myschool/dashboard", headers={
                "Cookie": f"ci_session={self.session_id}"
            })
            res.raise_for_status()
            return not res.ok
        except requests.RequestException:
            return True

    def create_session(self, username, password):
        found = self.__load_session()

        if not found or self.is_session_expired_or_invalid():
            res = requests.post(
                f"{self.base_url}/v1/teacherapp_v1/loginWithPassword",
                headers={
                    "User-Agent": self.user_agent,
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                data={
                    "LoginID": username,
                    "Password": str_to_md5(password),
                    "IsWebRequest": "Y"
                }
            )

            session_id = res.cookies.get("ci_session")

            self.session_id = session_id
            self.__dump_session()
        else:
            self.session_id = found

    def __get_secure(self, url):
        res = requests.get(f"{self.base_url}{url}", headers={
            "Cookie": f"ci_session={self.session_id}"
        })
        return res.text if res.status_code == 200 else None

    def get_user(self):
        return User(self.__get_secure("/v1/studentweb/profile"))

    def create_session_from_env(self, username_var, password_var):
        return self.create_session(os.getenv(username_var), os.getenv(password_var))
