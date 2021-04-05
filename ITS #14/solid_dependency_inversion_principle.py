class XMLHTTPService:
    @staticmethod
    def request(url, method):
        pass


class XMLHTTPRequest(XMLHTTPService):
    pass


class HTTPConnection:
    @staticmethod
    def connect(url, string, **options):
        return ''


class Http:
    def __init__(self, xml_http_service):
        self.__xml_http_service = xml_http_service

    def get(self, url, **options):
        self.__xml_http_service.request(url, 'GET')

    def post(self, url, options):
        self.__xml_http_service.request(url, 'POST')