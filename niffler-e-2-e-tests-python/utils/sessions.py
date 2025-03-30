from urllib.parse import parse_qs, urlparse
from utils.allure_helpers import allure_attach_request

from requests import Session


class BaseSession(Session):
    """Сессия с прокидыванием base_url и логированием запроса, ответа, хедеров ответа."""

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.base_url = kwargs.pop("base_url", "")

    # @raise_for_status
    @allure_attach_request
    def request(self, method, url, **kwargs):
        """Логирование запроса и вклейка base_url."""
        return super().request(method, self.base_url + url, **kwargs)


class AuthSession(Session):
    """Сессия с прокидыванием base_url и логированием запроса, ответа, хедеров ответа.
    + Авто сохранение cookies внутри сессии из каждого response и redirect response, и 'code' авторизации."""

    def __init__(self, *args, **kwargs):
        """
        Прокидываем base_url - url авторизации из энвов
        code - код авторизации из redirect_uri
        """
        super().__init__()
        self.base_url = kwargs.pop("base_url", "")
        self.code = None

    # @raise_for_status
    @allure_attach_request
    def request(self, method, url, **kwargs):
        """Сохраняем все cookies из redirect'a и сохраняем code авторизации из redirect_uri,
        И используем в дальнейшем в последующих запросах этой сессии."""

        response = super().request(method, self.base_url + url, **kwargs)
        for r in response.history:
            cookies = r.cookies.get_dict()
            self.cookies.update(cookies)
            code = parse_qs(urlparse(r.headers.get("Location")).query).get("code", None)
            if code:
                self.code = code

        return response
