import logging
from http.client import HTTPException

logger = logging.getLogger(__name__)


class HTTPError(HTTPException):
    def __init__(self, status_code: int, detail: str = None, error_code: str = None) -> None:
        super().__init__(status_code, detail)
        self.status_code = status_code
        self.error_code = error_code
        self.detail = detail
        logger.info(f"s{self.__class__.__name__}(status_code={self.status_code!r}"
                    f"error_message={self.detail!r})"
                    )


class BrokerConnectionError(Exception):
    pass
