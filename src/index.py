from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from dotenv import load_dotenv
import os
import uvicorn

from routes import lightswitch
load_dotenv()
app = FastAPI()

app.include_router(lightswitch.router)

@app.exception_handler(StarletteHTTPException)
async def error(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        custom_response = {
            "errorCode": "errors.com.lightweight.common.not_found",
            "errorMessage": "Sorry, the resource you were trying to find could not be found",
            "numericErrorCode": 1004,
            "originatingService": "any",
            "intent": "prod"
        }
        return JSONResponse(content=custom_response, status_code=404)
    else:
        return JSONResponse(content={"detail": exc.detail}, status_code=exc.status_code)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 3551))
    uvicorn.run(app, host="0.0.0.0", port=port)
