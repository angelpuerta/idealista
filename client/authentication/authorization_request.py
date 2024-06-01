import base64
from enum import Enum


class Scope(Enum):
    READ = "read"
    WRITE = "write"


class AuthorizationRequest:
    authorization: str
    content_type = "application/x-www-form-urlencoded"

    grant_type = "client_credentials"
    scope = Scope.READ

    def __init__(self, api_key, secret):
        base64_auth = base64.b64encode(f"{api_key}:{secret}".encode('ascii')).decode('ascii')
        self.authorization = f"Basic {base64_auth}"

    @property
    def headers(self):
        return {
            'Authorization': self.authorization,
            'Content-Type': self.content_type
        }

    @property
    def body(self):
        return {
            'grant_type': self.grant_type,
            'scope': self.scope.value
        }
