from fastapi import FastAPI, HTTPException
from typing import Optional

from method import shopee, shopee_keyword, shopee_seller

app = FastAPI()

@app.get("/shop/{username}/products")
async def get_products_from_shop(username: str):
    try:
        # Grab products from shop using original script logic
        product_list = shopee(username)
    except Exception:
        raise HTTPException(status_code=400, detail="Error occurred while getting products from shop.")
    return product_list

@app.get("/products/{keyword}/trending")
async def get_trending_products(keyword: str, location: Optional[str]=None):
    try:
        # Grab trending products using original script logic
        product_list = shopee_keyword(keyword, location)
    except Exception:
        raise HTTPException(status_code=400, detail="Error occurred while getting trending products.")
    return product_list

@app.get("/shops/{keyword}/list")
async def get_shop_list(keyword: str):
    try:
        # Grab list of shops using original script logic
        shop_list = shopee_seller(keyword)
    except Exception:
        raise HTTPException(status_code=400, detail="Error occurred while getting list of shops.")
    return shop_list