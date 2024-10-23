import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from databases import Database


load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

database = Database(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()   

async def get_db():
    db: AsyncSession = AsyncSessionLocal()
    try:
        yield db 
    finally:
        await db.close()
