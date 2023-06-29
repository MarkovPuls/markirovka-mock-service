from fastapi import FastAPI
from router import router as router_api

app = FastAPI(title="Mock_app")

app.include_router(router_api)
