from utils import StrEnum


class PeriodEnum(StrEnum):
    ONE_DAY = '1d'
    FIVE_DAY = '5d'
    ONE_MONTH = '1mo'
    THREE_MONTH = '3mo'
    SIX_MONTH = '6mo'
    ONE_YEAR = '1y'
    TWO_YEAR = '2y'
    FIVE_YEAR = '5y'
    TEN_YEAR = '10y'
    YTD = 'ytd'
    MAX = 'max'


class IntervalEnum(StrEnum):
    ONE_MINUTE = '1m'
    TWO_MINUTE = '2m'
    FIVE_MINUTE = '5m'
    FIVTEEN_MINUTE = '15m'
    THIRTY_MINUTES = '30m'
    SIXTY_MINUTES = '60m'
    NINENTY_MINUTES = '90m'
    ONE_HOUR = '1h'
    ONE_DAY = '1d'
    FIVE_DAYS ='5d'
    ONE_WEEK = '1wk'
    ONE_MONTH = '1mo'
    THREE_MONTHS = '3mo'
