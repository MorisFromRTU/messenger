from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .. import db, auth, security, schemas, crud
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()

@router.post('/login')
async def login(form_data: schemas.UserLogin, db: AsyncSession = Depends(db.get_db)):
    return await auth.login_for_access_token(form_data=form_data, db=db)

@router.post('/register')
async def register(user: schemas.UserRegister, db: AsyncSession = Depends(db.get_db)):
    return await auth.register_user(db=db, user=user)

@router.get('/token')
async def get_user_by_token(token: str, db: AsyncSession = Depends(db.get_db)):
    return await auth.get_current_user(token=token, db=db)