from sqlalchemy.ext.asyncio import AsyncSession
from .models import User
from .schemas import UserCreate, UserUpdate
from .repositories import UserRepository


class UserService:
    """
    Service layer for User operations.
    Encapsulates business logic and delegates persistence to UserRepository.
    """

    def __init__(self, repo: UserRepository):
        self.repo = repo

    @classmethod
    def with_session(cls, db: AsyncSession) -> "UserService":
        """
        Convenience constructor if you want to build the service directly
        from a database session (used in dependency injection).
        """
        return cls(UserRepository(db))

    async def register_user(self, payload: UserCreate) -> User:
        """
        Create a new user.
        Business rules (e.g., password hashing, uniqueness checks) can be added here.
        """
        return await self.repo.create(payload)

    async def find_user_by_id(self, user_id: int) -> User | None:
        """
        Retrieve a user by their ID.
        """
        return await self.repo.get_by_id(user_id)

    async def find_user_by_username(self, username: str) -> User | None:
        """
        Retrieve a user by their username.
        """
        return await self.repo.get_by_username(username)

    async def update_user(self, user: User, payload: UserUpdate) -> User:
        """
        Update user fields with provided payload.
        """
        return await self.repo.update(user, payload)

    async def delete_user(self, user: User) -> User:
        """
        Delete a user from the database.
        """
        return await self.repo.delete(user)
