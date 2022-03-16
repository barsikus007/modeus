from select import select
from sqlalchemy.orm import sessionmaker, selectinload
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel.sql.expression import Select, SelectOfScalar

from settings import settings


Select.inherit_cache = True
SelectOfScalar.inherit_cache = True

engine = create_async_engine(settings.DATABASE_URL, echo=settings.DEBUG)


async def get(session: AsyncSession, model, model_id: int):
    return (await session.exec(select(model).where(model.id == model_id).options(selectinload('*')))).first()


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
