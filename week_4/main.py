from fastapi import FastAPI
import uvicorn

from routes import test_routes, caesar_routes, fence_routes, summary_routes

app = FastAPI()

app.include_router(test_routes.router)
app.include_router(caesar_routes.router)
app.include_router(fence_routes.router)
app.include_router(summary_routes.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
