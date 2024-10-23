from fastapi import FastAPI
from .router import setup_routes

app = FastAPI()

setup_routes(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)