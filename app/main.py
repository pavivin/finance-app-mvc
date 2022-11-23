import random
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request

from views import Response
from controllers import ready, auth, stocks
from services.db import connect_db, init_db

import exceptions


app = FastAPI()
app.include_router(ready.router)
app.include_router(auth.router)
app.include_router(stocks.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.websocket(
    "/chart/{stock_id}/ws"
)
async def get_chart(websocket: WebSocket, stock_id: int):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        await websocket.send_json({"answer": data, "stock": random.random(), "stock_id": stock_id})


@app.on_event("startup")
async def startup():
    await connect_db(app)
    await init_db()


@app.exception_handler(Exception)
async def unicorn_base_exception_handler(request: Request, exc: Exception):
    error = exceptions.ServerError(debug=str(exc))

    return Response(
        code=error.status_code,
        payload=error.to_json(),
    )


@app.exception_handler(exceptions.ApiException)
async def unicorn_api_exception_handler(request: Request, exc: exceptions.ApiException):
    return Response(code=exc.status_code, payload=exc.to_json())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
