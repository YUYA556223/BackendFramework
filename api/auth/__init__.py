from exceptions.invalid_token import InvalidTokenException
from api.auth.account_info import AccountInfo
from api.auth._config import AuthConfig
from flask import Request
from api.auth.certificate import Certificate
from plugins.collections.generic import DictionaryC
from plugins.reflection.decorators import static


class AuthManager:
    __ucache = DictionaryC[str, Certificate]()

    @staticmethod
    def get_certificate(request: Request):
        token = request.headers.get("auth")
        if (token is None) or (token == ""):
            return None
        else:
            if AuthManager.__ucache.ContainsKey(token):
                return AuthManager.__ucache[token]
            AuthManager.__vertify_certificate_cache()
            auth = AuthConfig.firebase_config().auth()
            info = AccountInfo(auth.get_account_info(token))
            certificate = Certificate(info)
            return certificate

    @staticmethod
    def __vertify_certificate_cache() -> None:
        if AuthManager.__ucache.Length == AuthConfig.cache_count():
            AuthManager.__ucache.RemoveAt(0)
        pass
