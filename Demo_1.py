@app.get("/items/{item_id}", response_model=ItemCreate)
async def read_item(item_id: int):
    query = items.select().where(items.c.id from fastapi import FastAPI, HTTPException== item_id)
    item = await database.fetch_one(query)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {**item}


print("This is demo for Swapnil ")

print("End Line form Main Branch line# 12 ")