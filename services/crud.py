from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from db.models import Repository, Owner


async def create_owner(session: AsyncSession, name: str):
    async with session:
        owner = Owner(name=name)
        session.add(owner)
        await session.commit()
        await session.refresh(owner)

    return owner


async def get_owner(session: Session, name: str):
    async with session:
        query = select(Owner).where(Owner.name == name)
        owner = await session.scalar(query)

    return owner


async def create_repository(session: AsyncSession, name: str, owner_id: int, file_id: int = None):
    async with session:
        repository = Repository(name=name, owner_id=owner_id, file_id=file_id)
        session.add(repository)
        await session.commit()
        await session.refresh(repository)

    return repository


async def get_repository(session: Session, name: str, owner: Owner):
    async with session:
        query = select(Repository).where(Repository.name == name, Repository.owner == owner)
        repository = await session.scalar(query)

        return repository
