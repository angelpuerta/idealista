from dataclasses import dataclass

from client.authentication.authorization_request import Scope

@dataclass
class AuthorizationResponse:
    access_token: str
    token_type: str
    expires_in: int
    scope: Scope
    jti:str
