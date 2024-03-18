from fastapi import FastAPI
# from app.routes.category_routes import router as category_routes
from routes.produto_routes import router as produto_router
from routes.user_rourtes import router as user_router
# from app.routes.user_routes import router as user_routes
# from app.routes.poc import router as poc_routes


app = FastAPI()
@app.get('/health-check')
def health_check():
    return True
#TODO
# app.include_router(category_routes)
app.include_router(produto_router)
app.include_router(user_router)
# app.include_router(poc_routes)


if __name__ == "__main__":
    import uvicorn
#                  #nomearquivo#nomeAppMain   
    uvicorn.run("main:app", host="127.0.0.1", port=8003, reload=True)