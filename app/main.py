from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()
@app.include_router(router)

@app.get("/")
async def health():
    return {"status": "ok"}
