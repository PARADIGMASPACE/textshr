from fastapi import APIRouter ,status , Response , HTTPException , Request
from uuid import uuid4
from client.redis_client import RedisClient
import time
router = APIRouter(prefix="/v1/session", tags=["Session"])
redis_client = RedisClient()

def generate_uuid():
    return str(uuid4())

def generate_cookie(response: Response, session_id: str):
    response.set_cookie(
        key="session",
        value=session_id,
        httponly=True,
        secure=True,
        samesite="strict",
        path="/"
    )

async def session_set_redis(session_id: str):
        created_at = int(time.time())
        await redis_client.set(
            key=session_id,
            value={"created_at": created_at},
            ttl=30 * 24 * 3600,
        )



@router.post("/session_create", status_code=status.HTTP_201_CREATED)
async def create_session(response: Response):
    session_id = (generate_uuid())
    generate_cookie(response, session_id)
    await session_set_redis(session_id)
    return {"status":"created","session_id": session_id}



@router.post("/session_refresh", status_code=status.HTTP_200_OK)
async def session_refresh(request: Request , response: Response):
    session_id = request.cookies.get("session")
    if session_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,detail="No session cookie")
    exists = await redis_client.exists(session_id)
    if not exists:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired session")
    new_session_id = generate_uuid()
    generate_cookie(response, new_session_id)
    await redis_client.delete(session_id)
    await session_set_redis(new_session_id)
    return {"status":"refreshed"}

@router.post("/session_validate", status_code=status.HTTP_200_OK)
async def session_validate(request: Request):
    session_id = request.cookies.get("session")
    if session_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="No session cookie")
    exists = await redis_client.exists(session_id)
    if not exists:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid session cookie")
    return {"status":"valid"}


