from Connections import HTTPConnection


class AssetHandler:
    def __init__(self, connection: HTTPConnection):
        self.connection = connection
        self._build_uris()

    def _build_uris(self):
        self._uri_asset = 'api/v1/user/asset'

    def get(self):
        return self.connection.get(self._uri_asset)

    def update(self):
        pass
