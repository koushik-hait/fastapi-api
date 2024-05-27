from datetime import datetime, timedelta
import hashlib
from random import randbytes
from bson.objectid import ObjectId
from fastapi import APIRouter, Request, Response, status, Depends, HTTPException
from pydantic import EmailStr
from config import settings
from models import schemas



router = APIRouter()
ACCESS_TOKEN_EXPIRES_IN = settings.ACCESS_TOKEN_EXPIRES_IN
REFRESH_TOKEN_EXPIRES_IN = settings.REFRESH_TOKEN_EXPIRES_IN


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register(payload: schemas.CreateUserSchema, request: Request):
    pass

@router.post('/login')
def login(payload: schemas.LoginUserSchema, response: Response, ):
    pass

@router.get('/refresh')
def refresh_token(response: Response,):
    pass

@router.get('/logout', status_code=status.HTTP_200_OK)
def logout(response: Response):
    pass

@router.get('/verifyemail/{token}')
def verify_me(token: str):
    pass