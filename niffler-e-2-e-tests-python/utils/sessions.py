from urllib.parse import parse_qs, urlparse
from utils.allure_helper import allure_attach_request
from requests import Session
from utils.helper import step

class AuthSession(Session):
    """Сессия с логированием запроса, ответа, хедеров ответа.
    + Авто сохранение cookies внутри сессии из каждого response и redirect response, и 'code' авторизации."""
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.code = None

    @step
    # @allure_attach_request
    def request(self, method, url, **kwargs):
        """Сохраняем все cookies из redirect'a и сохраняем code авторизации из redirect_uri,
        И используем в дальнейшем в последующих запросах этой сессии."""

        response = super().request(method, url, **kwargs)
        for r in response.history:
            cookies = r.cookies.get_dict()
            self.cookies.update(cookies)
            code = parse_qs(urlparse(r.headers.get("Location")).query).get("code", None)
            if code:
                self.code = code

        return response
