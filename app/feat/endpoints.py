"""
Created on 2022-12-08 15:25
@author: johannes
"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse


router = APIRouter(
    prefix="/feat",
    tags=["feat"],
)


@router.get("/")
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Yellow</title>
        </head>
        <body>
            <h1>Yo yo !</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
