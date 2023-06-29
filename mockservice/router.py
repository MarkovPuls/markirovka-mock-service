from fastapi import APIRouter
import uuid

router = APIRouter(
    prefix="/api",
    tags=["api"]
)


@router.post("/v1/auth")
async def get_operations():
    try:
        return {'code': uuid.uuid4()}
    except ValueError as ex:
        return {
            "error": f"{ex}"
        }
