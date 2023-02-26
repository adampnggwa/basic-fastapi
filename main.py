from fastapi import FastAPI                         

app = FastAPI()

@app.get("/items/{item.id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
