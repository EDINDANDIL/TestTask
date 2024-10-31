from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
async def root(name: str = Query(..., alias="name"), message: str = Query(..., alias="message")):
    return {"message": f"Hello {name}! {message}!"}.get("message")