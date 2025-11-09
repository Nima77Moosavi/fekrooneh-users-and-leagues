from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()

# Correct usage: call include_router, not decorate
app.include_router(router)

@app.get("/")
async def health():
    return {"status": "ok"}
