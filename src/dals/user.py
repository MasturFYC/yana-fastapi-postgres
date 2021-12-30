''' User Dal '''
from typing import List
from sqlalchemy import select, update, delete
from sqlalchemy.orm import  Session
from src.models.user import User
from src.schemas.user import UserIn, UserLogin


class user_dal():
    ''' load User dal '''

    def __init__(self, session: Session):
        self.session = session

    async def user_get_all(self) -> List[User]:
        ''' load all Users '''
        query = await self.session\
            .execute(select(User).order_by(User.name))
        return query.scalars().all()

    async def user_get_one(self, pid: int) -> User:
        ''' load one User by id '''
        query = await self.session.execute(select(User)
                                           .where(User.id == pid))
        return query.scalars().first()
    
    async def user_get_user(self, payload: UserLogin) -> User:
        ''' load one User by id '''
        query = await self.session.execute(select(User)
                .where(User.email == payload.email, User.password == payload.password))
        return query.scalars().first()


    async def user_insert(self, payload: UserIn) -> User:
        ''' insert new User '''
        new_user = User(name=payload.name, email=payload.email,
                        password=payload.password, role=payload.role)
        self.session.add(new_user)
        await self.session.flush()
        return new_user

    async def user_update(self, pid: int, payload: UserIn) -> User:
        ''' update one User by id '''
        query = update(User).where(User.id == pid)\
            .values(name=payload.name, email=payload.email,
                    password=payload.password, role=payload.role).returning(User)
        query.execution_options(synchronize_session="fetch")
        res = await self.session.execute(query)
        tup = res.fetchone()
        await self.session.commit()
        
        return tup

    async def user_delete(self, pid: int) -> int:
        ''' delete User by id '''
        query = delete(User).where(
            User.id == pid).returning(User.id)
        res = await self.session.execute(query)
        tup = res.fetchone()
        await self.session.commit()
    
        return {'id': tup.id}

