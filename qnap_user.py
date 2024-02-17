import json


class QnapUser:
    """Connected Qnap user data"""

    _user_id: int = 0

    _sid: str = ""

    _q_token: str = ""

    _cuid: str = ""

    _username: str = ""

    def __init__(self, user_id: int,  sid: str, q_token: str, cuid: str, username: str) -> None:
        self._user_id = user_id
        self._sid = sid
        self._q_token = q_token
        self._cuid = cuid
        self._username = username

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def sid(self) -> str:
        return self._sid

    @property
    def q_token(self) -> str:
        return self._q_token

    @property
    def cuid(self) -> str:
        return self._cuid

    @property
    def username(self) -> str:
        return self._username

    def __str__(self) -> str:
        return self.to_json()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
