from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from .config import settings
from model.models import Book  # Ensure models are imported for metadata


engine = create_async_engine(settings.database_url, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session():
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


async def init_db() -> None:
    """Create tables declared with SQLModel models using the async engine."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def main():
    await init_db()
    print("Tables created (if not existing).")

