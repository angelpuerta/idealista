import json
import logging

import requests

from .authorization_request import AuthorizationRequest
from .authorization_response import AuthorizationResponse
from ..config import config

from utils.decorator import singleton


@singleton
class AuthenticationService:
    uri = f"{config.idealista_base_url}/oauth/token"

    def download_token(self):
        request = AuthorizationRequest(config.apiKey, config.secret)
        result = requests.post(
            self.uri,
            data=request.body,
            headers=request.headers
        )
        if result.status_code != 200:
            raise Exception(f'The request failed with code ${result.status_code}: ${result.text}')
        result = self.map(result)
        logging.debug(result)
        return result

    def map(self, response: requests.Response) -> AuthorizationResponse:
        return AuthorizationResponse(**response.json())


@singleton
class AuthenticationSession:
    service: AuthenticationService = AuthenticationService()
    _token: str = None

    @property
    def token(self) -> str:
        if not self._token:
            self._token = self.service.download_token().access_token
        return self._token

    def expire_token(self):
        self._token = None


authenticationSession = AuthenticationSession()
