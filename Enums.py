from enum import Enum, unique


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
