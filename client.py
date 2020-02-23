from Connections import HTTPConnection

# from Order import OrderHandler
# from Asset import AssetHandler
# from Investor import InvestorHandler


class Client:
    def __init__(self, url, username, password, broker_code):
        self._build_uris()
        self.connection = HTTPConnection(url, broker_code)
        login_data = self.login(username, password)
        print(login_data)
        print(login_data.text)
        print(login_data.json())
        # self.order = OrderHandler(self.connection)
        # self.asset = AssetHandler(self.connection)
        # self.investor = InvestorHandler(self.connection)

    def _build_uris(self):
        self._uri_login = 'api/v1/login'
        self._uri_logout = 'api/v1/logout'

    def login(self, username: str, password: str):
        return self.connection.post(self._uri_login, {
            'username': username,
            'password': password
        })

    def logout(self):
        return self.connection.post(self._uri_logout)


c = Client('https://oms8.irbroker.com/', 'shahramitisuser', '5xxLJqbjUHkD',
           776)
