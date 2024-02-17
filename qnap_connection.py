import requests
import guard
from common_tools import nameof, ping
from qnap_user import QnapUser
from get_sid_tools import ezEncode, utf16to8
from bs4 import BeautifulSoup


class QnapConnection:
    """
    QNap connection class.
    """

    _ip_address: str = ""

    _port: str = ""

    _connection_address: str = ""

    def __init__(self, ip_address: str, port: str) -> None:
        guard.is_not_empty(ip_address, nameof(ip_address))
        guard.is_not_empty(port, nameof(port))
        if not ping(ip_address):
            raise ValueError(f"Incorrect connection data. Cannot ping {ip_address}.")

        self._ip_address = ip_address
        self._port = port
        self._connection_address = f"{self._ip_address}:{self._port}"

    @property
    def connection_address(self):
        return self._connection_address

    def connect_via_password(self, username: str, password: str) -> QnapUser:
        """
        Authenticates user's account via password.
        :param username: Login username.
        :param password: Login password.
        :return: Qnap user authentication data.
        """
        guard.is_not_empty(username, nameof(username))
        guard.is_not_empty(password, nameof(password))

        encoded_password = ezEncode(utf16to8(password))
        request_str = f"http://{self._connection_address}/cgi-bin/authLogin.cgi?user={username}" \
                      f"&pwd={encoded_password}&remme=1&r=0.802557202605028"
        return self._get_qnap_user(request_str, username)

    def connect_via_qtoken(self, username: str, qtoken: str) -> QnapUser:
        """
        Authenticates user's account via qtoken.
        :param username: Login username.
        :param qtoken: Login qtoken.
        :return: Qnap user authentication data.
        """
        guard.is_not_empty(username, nameof(username))
        guard.is_not_empty(qtoken, nameof(qtoken))

        request_str = f"http://{self._connection_address}/cgi-bin/authLogin.cgi?user={username}" \
                      f"&qtoken={qtoken}&remme=1&r=0.802557202605028"
        return self._get_qnap_user(request_str, username)

    def _get_qnap_user(self, request_str: str, username: str) -> QnapUser:
        """
        Returns Qnap user authentication data.
        :param request_str: Request string.
        :param username: Login username.
        :return: Qnap user authentication data.
        """
        response = requests.get(request_str)
        if response.status_code != requests.codes.ok:
            raise ConnectionError(f"Cannot connect to user {username}")

        soup = BeautifulSoup(response.content, 'xml')
        authPassed = int(soup.authPassed.string)
        if authPassed == 0:
            raise ValueError(f"Cannot connect to user {username}")

        user_id = soup.userid.string
        sid = soup.authSid.string
        qtoken = soup.qtoken.string
        cuid = soup.cuid.string
        response_username = soup.username.string
        qnap_user = QnapUser(user_id, sid, qtoken, cuid, response_username)
        print(qnap_user)
        return qnap_user
