# from fastapi import FastAPI
# from routers import user, article

# app = FastAPI()

# app.include_router(user.router)
# app.include_router(article.router)
# # main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}