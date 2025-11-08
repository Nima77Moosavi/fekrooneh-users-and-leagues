from fastapi import FastAPI

app = FastAPI()

app.get("/health")

@app.get("/")
async def health():
    return {"status": "ok"}
