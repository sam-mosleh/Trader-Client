from Connections import HTTPConnection
from Enums import CoreType, MarketType, OrderSide, ValidityType


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
