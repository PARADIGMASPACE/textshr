from fastapi import FastAPI

from routes.session import router as session_router
# from routes.test import router as test_router
app = FastAPI(title="Session Service")

app.include_router(session_router)
# app.include_router(test_router)


@app.get("/")
def read_root():
    return {"session_service": "active"}

