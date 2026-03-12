from app.server.app import app
import uvicorn
from app.core.config import settings


def main():
    uvicorn.run("main:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=settings.DEBUG, workers=5)
    print("hello new")


if __name__ == "__main__":
    main()
