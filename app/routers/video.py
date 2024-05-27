from fastapi import APIRouter, Request, Response, status, Depends, HTTPException
from typing import Annotated
from fastapi import FastAPI, File, UploadFile

router = APIRouter()

@router.post("/all-video/")
async def get_all_video():
    return {}

@router.post("/watch/{vid}/")
async def get_video_by_id(vid: str):
    return {"id":vid}

@router.post("/upload-video/")
async def add_video(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    return {"filenames": [file.filename for file in files]}