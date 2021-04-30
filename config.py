from __future__ import annotations

import abc
import base64
from enum import Enum
from typing import Any, List, Literal, Optional, Type, Union

import flask
from dash_auth.auth import Auth
from pydantic import BaseModel, BaseSettings, validator


class AuthorizationError(Exception):
    pass


class RoleEnum(Enum):
    """User role """

    admin: int = 1
    guest: int = 2

    def __le__(self, other: Any) -> Union[bool, NotImplemented]:
        """Define hierarchy logic."""
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def has_access(self, access_level: RoleEnum) -> bool:
        """Implement access control there"""
        if self == RoleEnum.admin:
            return True

        return self <= access_level


class CustomAuth(Auth, metaclass=abc.ABCMeta):
    def get_role(self):
        raise NotImplementedError


class NoAuth(CustomAuth):
    """Bypass authentication."""

    def __init__(self, dash_app, *args, **kwargs):
        Auth.__init__(self, dash_app)

    def is_authorized(self) -> bool:
        return True

    def auth_wrapper(self, f):
        return f

    def index_auth_wrapper(self, f):
        return f

    def login_request(self):
        # Must implement abstract base method, even if empty
        pass

    def get_role(self) -> int:
        return RoleEnum.admin


class UserIn(BaseModel):
    login: str
    pwd: str
    role: RoleEnum


class BasicRBACAuth(CustomAuth):
    def __init__(self, dash_app, list_authorized_users: List[UserIn]):
        Auth.__init__(self, dash_app)

        self._users = {
            user.login: {"pwd": user.pwd, "role": user.role}
            for user in list_authorized_users
        }

    @staticmethod
    def _extract_user_pwd_header():
        header = flask.request.headers.get("Authorization", None)
        if not header:
            raise AuthorizationError
        username_password = base64.b64decode(header.split("Basic ")[1])
        username_password_utf8 = username_password.decode("utf-8")
        username, password = username_password_utf8.split(":", 1)
        return username, password

    def is_authorized(self) -> bool:
        try:
            username, password = self._extract_user_pwd_header()
        except AuthorizationError:
            return False
        return self._users.get(username, {}).get("pwd") == password

    def get_role(self) -> int:
        username, _ = self._extract_user_pwd_header()
        return self._users[username]["role"]

    def login_request(self):
        return flask.Response(
            "Login Required",
            headers={"WWW-Authenticate": 'Basic realm="User Visible Realm"'},
            status=401,
        )

    def auth_wrapper(self, f):
        def wrap(*args, **kwargs):
            if not self.is_authorized():
                return flask.Response(status=403)

            response = f(*args, **kwargs)
            return response

        return wrap

    def index_auth_wrapper(self, original_index):
        def wrap(*args, **kwargs):
            if self.is_authorized():
                return original_index(*args, **kwargs)
            else:
                return self.login_request()

        return wrap


class Settings(BaseSettings):
    """Configuration class.

    Auto populate values from the environment.
    """

    language: Literal["fr", "en"] = "fr"

    debug: bool = True

    tracking_code: str = "UA-75404337-15"

    authenticator: Type[CustomAuth] = NoAuth
    users: Optional[List[UserIn]] = None

    @validator("users", pre=True, each_item=True)
    def _validate_users(cls, v):
        role_str = v.get("role", "guest")
        v["role"] = getattr(RoleEnum, role_str)
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
