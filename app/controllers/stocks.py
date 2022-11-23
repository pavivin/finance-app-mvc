from fastapi import APIRouter
from views.stocks import PeriodEnum, IntervalEnum
from services.invest import InvestService
from views import Response


router = APIRouter(tags=["portfolio"], prefix='/portfolio')


@router.get(
    "/stocks",
    # response_model=Response,
    summary="Simple health check.",
)
async def ready_check():
    return Response(payload={})


@router.get(
    "/stocks/{stock_id}",
    # response_model=Response,
    summary="Simple health check.",
)
async def ready_check():
    return Response(payload={})


@router.get(
    "/history",
    # response_model=Response,
    summary="Simple health check.",
)
async def ready_check(ticker: str, period: PeriodEnum, interval: IntervalEnum):
    info = InvestService.get_history_data_by_ticker(ticker_name=ticker, period=period, interval=interval)
    return Response(payload=info)
