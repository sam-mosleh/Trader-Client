import pprint
from enum import Enum, unique

import requests


@unique
class OrderStatus(Enum):
    DeleteOrderCauseByCoreError = -3
    OrderCompletelyExecuted = -2
    ForceToDeleteOrder = -1
    SentToCore = 0
    OrderInQueue = 2
    WaitForBank = 3


@unique
class OrderSide(Enum):
    Buy = 'SIDE_BUY'
    Sell = 'SIDE_SALE'


@unique
class ValidityType(Enum):
    Day = 'VALIDITY_TYPE_DAY'
    GoodTillCanceled = 'VALIDITY_TYPE_GOOD_TILL_CANCELED'
    FillOrKill = 'VALIDITY_TYPE_FILL_OR_KILL'
    GoodTillDate = 'VALIDITY_TYPE_GOOD_TILL_DATE'


@unique
class CoreType(Enum):
    StockExchange = 'c'
    IPO = 'i'
    FutureExchange = 'cf'


@unique
class MarketType(Enum):
    Stock = 'TSE_STOCK'
    IPO = 'TSE_IPO'
    IME_FUTURE = 'IME_FUTURE'


class HTTPConnection:
    def __init__(self, url: str, broker_code: int):
        self.url = url
        self.headers = {
            'device-type': '11',
            'broker-code': str(broker_code),
            'content-type': 'application/json'
        }
        self.session = requests.Session()
        self._build_uris()

    def get(self, uri, params):
        get_url = self.url + uri
        return self.session.get(
            get_url,
            params=params,
            headers=self.headers,
        )

    def post(self, uri: str, data={}):
        post_url = self.url + uri
        print(post_url)
        print(data)
        return self.session.post(post_url, json=data, headers=self.headers)

    def put(self, uri: str, data={}):
        post_url = self.url + uri
        return self.session.put(post_url, data=data, headers=self.headers)

    def delete(self, uri: str):
        delete_url = self.url + uri
        return self.session.delete(delete_url)

    def set_token(self, authToken):
        self.headers['authToken'] = authToken

    def buying_power(self):
        return self.get(self._uri_buying_power)


class RealtimeConnection:
    pass


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


class OrderHandler:
    def __init__(self, connection: HTTPConnection):
        self.connection = connection
        self._build_uris()

    def _build_uris(self):
        self._uri_order = 'api/v1/order'

    def new(self,
            instrument_id: str,
            side: OrderSide,
            quantity: int,
            disclosed_quantity: int,
            minimum_quantity: int,
            price: int,
            validity_type: ValidityType,
            core_type: CoreType = CoreType.StockExchange,
            market_type: MarketType = MarketType.Stock,
            validity_date='',
            order_type='ORDER_TYPE_LIMIT',
            bank_account_id=-1):
        return self.connection.post(
            self._uri_order, {
                'bankAccountId': bank_account_id,
                'insMaxLcode': instrument_id,
                'side': side.value,
                'quantity': quantity,
                'disclosedQuantity': disclosed_quantity,
                'minimumQuantity': minimum_quantity,
                'price': price,
                'orderType': order_type,
                'validityType': validity_type.value,
                'validityDate': validity_date,
                'coreType': core_type.value,
                'marketType': market_type.value
            })

    def edit(self,
             order_id: str,
             quantity: int,
             remaining_quantity: int,
             disclosed_quantity: int,
             price: int,
             validity_type: ValidityType,
             core_type: CoreType,
             market_type: MarketType,
             validity_date='',
             order_type='ORDER_TYPE_LIMIT'):
        return self.connection.put(
            self._uri_order, {
                'id': order_id,
                'quantity': quantity,
                'remainingQuantity': remaining_quantity,
                'disclosedQuantity': disclosed_quantity,
                'price': price,
                'orderType': order_type,
                'validityType': validity_type.value,
                'validityDate': validity_date,
                'coreType': core_type.value,
                'marketType': market_type.value
            })

    def delete(self, order_id: str, core_type: CoreType):
        return self.connection.delete(self._uri_order +
                                      '/{}/{}'.format(order_id, core_type))


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
