from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse

from app.controller import listing

app = FastAPI()

router = APIRouter()
router.include_router(listing.router, prefix='/listing', tags=['listings'])


@router.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Coding Assignment</title>
        </head>
        <body>
            <h1>Coding Assignment</h1>
            This is a coding assignment implementation that provides a simple CRUD API for property listings. <br />
            Details can be accessed using <a href="/docs">Swagger UI</a> or <a href="/redoc">Redoc UI</a>.
        </body>
    </html>
    """


app.include_router(router)
