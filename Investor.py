from Connections import HTTPConnection


class InvestorHandler:
    def __init__(self, connection: HTTPConnection):
        self.connection = connection
        self._build_uris()

    def _build_uris(self):
        self._uri_buying_power = 'api/v1/user/buyingPower'

    @property
    def buying_power(self):
        return self.connection.get(self._uri_buying_power)

    def update(self):
        pass
