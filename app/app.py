from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from config import settings
from routers import auth, video, aiml

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, tags=['Auth'], prefix='/api/v1/auth')
app.include_router(video.router, tags=['Video'], prefix='/api/v1/video')
app.include_router(aiml.router, tags=['Aiml'], prefix='/api/v1/aiml')


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}