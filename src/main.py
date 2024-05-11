# thirdparty
import uvicorn

# project
from logger import logger_initializing
from src import config
from src.app_initializer import get_fastapi_application


logger_initializing()
app = get_fastapi_application()


@app.get("/")
async def root() -> dict:
    return {"Status": "Application in progress"}


if __name__ == "__main__":
    uvicorn.run(app, host=config.app_config.host, port=config.app_config.port)
