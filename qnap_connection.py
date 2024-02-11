import requests
from qnap_user import QnapUser
from get_sid_tools import ezEncode
from bs4 import BeautifulSoup


class QnapConnection:
    """QNap connection class"""

    _ip_address: str = ""

    _port: str = ""

    _connection_address: str = ""

    def __init__(self, ip_address: str, port: str) -> None:
        self._ip_address = ip_address
        self._port = port
        self._connection_address = f"{self._ip_address}:{self._port}"

    def connect(self, username: str, password: str) -> QnapUser:
        encoded_password = ezEncode(password)
        request_str = f"http://{self._connection_address}/cgi-bin/authLogin.cgi?user={username}&pwd={encoded_password}&remme=1"
        response = requests.get(request_str)
        if response.status_code != requests.codes.ok:
            raise Exception(f"Cannot connect to user {username}")

        soup = BeautifulSoup(response.content, 'xml')
        user_id = soup.userid.string
        sid = soup.authSid.string
        qtoken = soup.qtoken.string
        cuid = soup.cuid.string
        response_username = soup.username.string
        qnap_user = QnapUser(user_id, sid, qtoken, cuid, response_username)
        print(qnap_user)
        return qnap_user