from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import UserCreate, UserRead, UserUpdate
from services import UserService
from dependencies import get_user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead)
async def create_user(
    payload: UserCreate,
    service: UserService = Depends(get_user_service)
):
    return await service.register_user(payload)

@router.get("/{user_id}", response_model=UserRead)
async def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    user = await service.find_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserRead)
async def update_user(
    user_id: int,
    payload: UserUpdate,
    service: UserService = Depends(get_user_service)
):
    user = await service.find_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await service.update_user(user, payload)

@router.delete("/{user_id}", response_model=UserRead)
async def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    user = await service.find_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await service.delete_user(user)
