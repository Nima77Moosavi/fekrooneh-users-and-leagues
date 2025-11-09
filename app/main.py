from fastapi import FastAPI, APIRouter
from app.users.routers import router as users_router


app = FastAPI()

router = APIRouter()

# Correct usage: call include_router, not decorate
app.include_router(users_router)

@app.get("/")
async def health():
    return {"status": "ok"}
