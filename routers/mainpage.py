import os,sys,inspect
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from fastapi import APIRouter, HTTPException, status, Depends
from repository import mainpage


router = APIRouter(
    tags = ["Home"]
)

@router.get("/")
def home():
    return mainpage.home({})